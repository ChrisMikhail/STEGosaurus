from PIL import Image
import numpy as np

def get_image_object(path_to_image):
    """Receives a path to an image, path_to_image and returns the generated PIL object, im."""

    try:
        with Image.open(path_to_image) as im:
            return im
    except:
        print(path_to_image)
        exit("Invalid image URL")