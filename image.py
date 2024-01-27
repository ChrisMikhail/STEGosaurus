from PIL import Image
import numpy as np


def get_image_object(path_to_image):
    """Receives a path to an image, path_to_image and returns the generated PIL object, im."""
    try:
        with Image.open(path_to_image) as im:
            return im
    except:
        exit(f"{path_to_image} is an invalid image URL")


def convert_to_binary(ciphertext):
    """Converts hex value into binary"""
    hex_bytes = bytes.fromhex(ciphertext)
    numpy_array = np.frombuffer(hex_bytes, dtype=np.uint8)
    binary_representation = np.unpackbits(numpy_array)
    return binary_representation


def convert_to_bytes(binary_representation):
    """Converts binary rep back to bytes for decryption"""
    bytes_array = np.packbits(binary_representation)
    bytes_object = bytes(bytes_array)
    return bytes_object
