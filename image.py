from PIL import Image
import numpy as np


def introduce_program():
    """Introduces program and gets path to image from user."""

    path_to_image = input("Welcome to STEGosaurus! Enter the path to an image to get started: ")
    return path_to_image


def get_image_object(path_to_image):
    """Receives a path to an image, path_to_image and returns the generated PIL object, im."""

    try:
        with Image.open(path_to_image) as im:
            return im
    except:
        exit("Invalid image URL")


if __name__ == '__main__':
    path_to_image = introduce_program()
    image_object = get_image_object(path_to_image)
