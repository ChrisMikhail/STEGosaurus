from encryption import generate_key, encrypt, decrypt
from image import get_image_object, convert_to_binary, convert_to_bytes


def introduce_program():
    """Introduces program and gets path to image and message to encrypt from user."""
    path_to_image = input("Welcome to STEGosaurus! Enter the path to an image to get started: ")
    message = input("Now, enter a message to hide in the image: ")
    return path_to_image, message


if __name__ == '__main__':
    path_to_image, message = introduce_program()
    image_object = get_image_object(path_to_image)
    key = generate_key()
    nonce, ciphertext, tag = encrypt(message, key)
    binary_representation = convert_to_binary(ciphertext.hex())
    ciphertext = convert_to_bytes(binary_representation)
    decrypt(nonce, ciphertext, tag, key)