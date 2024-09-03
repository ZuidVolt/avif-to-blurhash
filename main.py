from typing import Tuple, Optional
import numpy as np
from PIL import Image
import base64
import blurhash  # type: ignore[import]
from pathlib import Path


def generate_blurhash(image_path: Path) -> Tuple[Optional[str], Optional[str]]:
    """
    Generates a BlurHash and a base64-encoded PNG data URL for an AVIF image.

    :param image_path: Path to the AVIF image file.
    :return: A tuple containing the BlurHash string and the base64-encoded PNG data URL.
    """
    try:
        # Attempt to open the AVIF image
        with Image.open(image_path) as image:
            # Ensure the image is in RGB format
            if image.mode != "RGB":
                image = image.convert("RGB")

            # Get the original image size
            original_width, original_height = image.size

            # Calculate the maximum dimension for the resized image
            max_dimension = 64
            width = min(original_width, max_dimension)
            height = int(original_height * (width / original_width))
            # Resize image for BlurHash encoding, maintaining aspect ratio
            small_image = image.resize((width, height))

            # Convert image to numpy array
            image_array = np.array(small_image)

            # Generate BlurHash
            blurhash_str = blurhash.encode(image_array, 4, 4)

            # Convert resized image to PNG and then to base64
            temp_file_path = Path("temp.png")
            small_image.save(temp_file_path, "PNG")
            png_bytes = temp_file_path.read_bytes()
            base64_png = base64.b64encode(png_bytes).decode("utf-8")
            data_url = f"data:image/png;base64,{base64_png}"
            temp_file_path.unlink()  # Remove temporary file

            return blurhash_str, data_url

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None, None


def main():
    avif_image_path = Path("image.avif")  # Replace with your AVIF image file path

    blurhash_str, data_url = generate_blurhash(avif_image_path)

    if blurhash_str and data_url:
        print(f"Data URL: {data_url}\n")
        print(f"BlurHash: {blurhash_str}\n")
    else:
        print("Failed to generate BlurHash and Data URL.")


if __name__ == "__main__":
    main()
