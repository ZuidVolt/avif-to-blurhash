**BlurHash Generator for AVIF Images**
=====================================

A Python script to generate BlurHash strings and base64-encoded PNG data URLs for AVIF images.

**Table of Contents**
-----------------

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Example Output](#example-output)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)

**Introduction**
---------------

This project provides a simple Python script to generate BlurHash strings and base64-encoded PNG data URLs for AVIF images. BlurHash is a compact representation of an image that can be used as a placeholder before the actual image is loaded.

**Features**
------------

* Generates BlurHash strings for AVIF images
* Generates base64-encoded PNG data URLs for resized images
* Maintains aspect ratio while resizing images
* Supports images with RGB mode

**Requirements**
---------------

* Python 3.x
* Pillow (PIL) library (install using `pip install "pillow[avif]`)
* NumPy library
* base64 library
* blurhash library (install using `pip install blurhash`)

**Usage**
-----

1. Clone the repository: `git clone https://github.com/ZuidVolt/avif-to-blurhash`
2. Install the required libraries: `pip install -r requirements.txt`
3. Replace `image.avif` with your AVIF image file path in the `main.py` file
4. Run the script: `python3 main.py`

**Example Output**
-----------------

`BlurHash: L6P00;~q%M%1-;%M%1-;%M%1-;%M`

**Troubleshooting**
-----------------

* If you encounter issues with image processing, ensure that the image file is in the correct format (AVIF) and that the file path is correct.
* They could be issues with installing the avif Variant of pillow try using `pip install "pillow[avif]"` (remember to uninstall the normal pillow first)
* If you're using a virtual environment, make sure it's activated before running the script.

**Contributing**
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

**License**
-------

This project is licensed under the Apache License, Version 2.0 with Additional commercial term. See the [LICENSE](LICENSE) file for details.
