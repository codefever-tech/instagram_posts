from PIL import Image
import numpy as np

# ASCII characters from dark to light
ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(image_path, output_width=100, char_aspect=2.1):
    image = Image.open(image_path)
    width, height = image.size
    new_height = int((height / width) * output_width / char_aspect)
    image = image.resize((output_width, new_height)).convert('L')  # Grayscale
    
    pixels = np.array(image) # convert to a 2D array of pixels
    # mapping the pixel values to the ASCII characters
    ascii_art = "\n".join(
        "".join(ASCII_CHARS[int(pixel / 255 * (len(ASCII_CHARS) - 1))] for pixel in row)
        for row in pixels
    )
    # saving the ascii art in a txt file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_art)
    
    print(ascii_art)

image_to_ascii("ferrari-logo.jpg", output_width=100)
