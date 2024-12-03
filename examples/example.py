# examples/example.py
from src.image_converter import convert_image

# Example usage
input_path = "../images/example.jpg"
output_path = "../images/example.png"

convert_image(input_path, output_path)
print(f"Image converted successfully from {input_path} to {output_path}")
