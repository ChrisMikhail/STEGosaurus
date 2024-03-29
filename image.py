from PIL import Image
import numpy as np


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


def change_image(path, binary_representation, new_image_path):
    """Replace last bit of green channel with ciphertext as binary data"""
    with Image.open(path) as im:
        pixels = im.load()
        w, h = im.size
        if len(binary_representation) > w*h:
            return False
        else:
            idx = 0
            for x in range(w):
                for y in range(h):
                    current_colour = pixels[x, y]
                    if idx >= len(binary_representation):
                        break
                        # Replace last bit with binary_representation[idx]
                    current_colour = (
                        current_colour[0], current_colour[1] & 0b11111110 | binary_representation[idx], current_colour[2])
                    pixels[x, y] = current_colour
                    idx += 1
        im.save(new_image_path)
        return True


def extract_last_bit(length, new_image_path="example/sus_steg.png"):
    """Extracts last bits of binary data for the green channel of each pixel"""
    binary_data = []
    idx = 0
    with Image.open(new_image_path) as im:
        pixels = im.load()
        w, h = im.size

        for x in range(w):
            for y in range(h):
                current_colour = pixels[x, y]
                if idx >= length:
                    break
                    # Get least significant bit in binary
                last_bit = current_colour[1] & 1
                binary_data.append(last_bit)
                idx += 1
    return np.array(binary_data)
