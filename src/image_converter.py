from PIL import Image
import os

def convert_image(input_path, output_format):
    """
    Converts an image to a specified format.

    Args:
        input_path (str): Path to the input image file.
        output_format (str): Desired format ('png', 'jpeg', 'bmp', 'gif').

    Returns:
        str: Path to the converted image file.
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Construct output file name
            output_path = f"{os.path.splitext(input_path)[0]}.{output_format}"
            img.save(output_path, format=output_format.upper())
            return output_path
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    input_file = input("Enter the path to the image: ")
    format_choice = input("Enter the desired format (png, jpeg, bmp, gif): ").lower()

    output_file = convert_image(input_file, format_choice)
    if output_file:
        print(f"Image converted successfully: {output_file}")
    else:
        print("Image conversion failed.")