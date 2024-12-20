# Image Converter (Python)

Image Converter - Python is a lightweight Python script that enables users to convert images between multiple formats, including PNG, JPEG, GIF, and BMP. This tool is designed for simplicity and ease of use in small projects or quick image processing tasks.

## Features

- Converts images to/from multiple formats: PNG, JPEG, GIF, BMP.
- Simple and easy-to-use interface.
- Supports batch processing of images (optional with minor modifications).
- Lightweight and minimal dependencies.

## Requirements

- Python 3.6 or higher.
- Pillow library for image processing.

## Installation

1. Clone or download the repository:
    ```bash
    git clone https://github.com/marwan-ahmed-23/image-converter-python.git
    cd image-converter-python
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Here's how to use the `image_converter.py` script:

1. Place the image you want to convert in the `images/` directory.

2. Run the script and specify the input file, output file, and format:
   
    ```bash
    python src/image_converter.py images/input_image.jpg images/output_image.png
    ```

### Example

```bash
python src/image_converter.py images/example.jpg images/example.png
```

This will convert `example.jpg` to `example.png` and save it in the same directory.

## Directory Structure

image-converter-python/                                                                                                                
├── src/                                                                                                            
│   └── image_converter.py  # Main conversion script                                                                                            
├── images/                 # Folder for input and output images                                                            
├── examples/                                                                                                
│   └── example.py          # Example usage of the script                                                                            
├── requirements.txt        # Dependencies                                                                                
├── .gitignore                                                                                                    
└── README.md                                                                                            

## Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   
    ```bash
    git checkout -b feature-branch
    ```

3. Make your changes and commit them:

    ```bash
    git commit -m "Add new feature"
    ```

4. Push to your branch:

    ```bash
    git push origin feature-branch
    ```

5. Open a Pull Request.


