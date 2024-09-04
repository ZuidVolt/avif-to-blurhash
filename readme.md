
# BlurHash Generator for AVIF Images

A Python script to generate BlurHash strings and base64-encoded PNG data URLs for AVIF images.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Example Output](#example-output)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

This project provides a Python script for generating BlurHash strings and base64-encoded PNG data URLs from AVIF images. BlurHash is a compact representation of an image, ideal for creating placeholders while the full image loads, enhancing user experience and website performance.

## Features

- Generate BlurHash strings for AVIF images
- Create base64-encoded PNG data URLs for resized images
- Maintain aspect ratio during image resizing
- Support for RGB mode images
- Optimize image loading and improve website performance

## Requirements

- Python 3.6 or higher
- Pillow (PIL) library with AVIF support
- NumPy library
- base64 library
- blurhash library

## Installation

1. Clone the repository:

   ```markdown
   git clone https://github.com/ZuidVolt/avif-to-blurhash
   ```

2. Navigate to the project directory:

   ```markdown
   cd avif-to-blurhash
   ```

3. Install the required libraries:

   ```markdown
   pip install -r requirements.txt
   ```

## Usage

1. choose the input file directory you want to use with the -d Argument.

   ```markdown
   python3 main.py -d /path/to/file
   ```

   or if no file directory is Selected it will use `image.avif` in the main directory

2. Replace `image.avif` in the `main.py` file with your AVIF image file path.
Run the script:

   ```markdown
   python3 main.py
   ```

## Example Output

```markdown
BlurHash: L6P00;~q%M%1-;%M%1-;%M%1-;%M
```

## Troubleshooting

- Ensure the image file is in AVIF format and the file path is correct.
- For issues with Pillow's AVIF support, try:

  ```markdown
  pip uninstall pillow
  pip install "pillow[avif]"
  ```

- Activate your virtual environment before running the script, if applicable.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License

This project is licensed under the Apache License, Version 2.0 with important additional terms, including specific commercial use conditions. Users are strongly advised to read the full [LICENSE](LICENSE) file carefully before using, modifying, or distributing this work. The additional terms contain crucial information about liability, data collection, indemnification, and commercial usage requirements that may significantly affect your rights and obligations.

---

Keywords: BlurHash, AVIF, image processing, Python, base64, PNG, data URL, image optimization, web performance
