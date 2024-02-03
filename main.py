from encryption import generate_key, encrypt, decrypt
from image import (get_image_object, convert_to_binary, convert_to_bytes, change_image, extract_last_bit)
from open_yaml import read_yaml_file

def introduce_program():
    """Introduces program and gets path to image and message to encrypt from user."""
    name_of_image = input("Welcome to STEGosaurus! Enter the name of an image to get started: ")
    new_image_name = input("Enter the name of your new image, it will be saved in the static folder of this project: ")
    message = input("Now, enter a message to hide in the image: ")
    return name_of_image, new_image_name, message


if __name__ == '__main__':
    name_of_image, new_image_name, message = introduce_program()
    path_to_image = f"static/{name_of_image}.png"
    path_to_new_image = f"static/{new_image_name}.png"
    image_object = get_image_object(path_to_image)
    key = generate_key()
    nonce, ciphertext, tag = encrypt(message, key)
    binary_representation = convert_to_binary(ciphertext.hex())
    change_image(path_to_image, binary_representation, new_image_name)
    decrypted_binary = extract_last_bit(f"static/{new_image_name}.png", len(binary_representation))
    decrypted_ciphertext = convert_to_bytes(decrypted_binary)
    message = decrypt(nonce, decrypted_ciphertext, tag, key)
    image_collage(path_to_image, path_to_new_image, "static/new.png")

