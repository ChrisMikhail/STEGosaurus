from encryption import generate_key, encrypt, decrypt, write_to_yaml
from image import get_image_object, convert_to_binary, convert_to_bytes, change_image, extract_last_bit
from open_yaml import read_yaml_file
import os


def decode_image(path_to_yaml="keys/secrets.yaml", path_to_new="static/sus_steg.png"):
    """Decodes image given a yaml path and a path to a png"""
    example_key, example_nonce, example_tag, example_length = read_yaml_file(path_to_yaml)
    example_extracted_binary = extract_last_bit(example_length, path_to_new)
    example_decrypted_ciphertext = convert_to_bytes(example_extracted_binary)
    example_message = decrypt(example_nonce, example_decrypted_ciphertext, example_tag, example_key)
    return example_message


def encode_image(path, path_to_new, message_to_encode, yaml_location):
    # Encryption of data
    key = generate_key()  # Random AES key
    nonce, ciphertext, tag = encrypt(message_to_encode, key)
    binary_rep = convert_to_binary(ciphertext.hex())  # Binary representation of encrypted bytes data
    bin_length = len(binary_rep)
    write_to_yaml(key, nonce, tag, bin_length, yaml_location)
    # Changing the image
    change_image(path, binary_rep, path_to_new)


def introduce_program():
    """Introduces program and gets path to image and message to encrypt from user."""
    image_name = input("Welcome to STEGosaurus! Enter the name of your image in the static folder to get started ("
                       "Don't include file extension): ")
    name_of_new_image = input("Enter the name of your new image, it will be saved in the static folder of this "
                              "project: ")
    message_to_encode = input("Now, enter a message to hide in the image: ")
    return image_name, name_of_new_image, message_to_encode


if __name__ == '__main__':
    input(
        "Hello, there! The original image is in the static folder and is named steg and the secret message is in "
        "sus_steg. Press any key to see what the message!")
    print(decode_image())
    # Unpack basic data
    name_of_image, new_image_name, message = introduce_program()
    path_to_image = f"static/{name_of_image}.png"  # Original image path
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    path_to_new_image = os.path.join(downloads_folder, f"{new_image_name}.png")  # Path for new image
    image_object = get_image_object(path_to_image)  # Generates a PIL image object
    new_yaml_location = f"keys/{new_image_name}_secrets.yaml"

    # Encryption of data
    key = generate_key()  # Random AES key
    nonce, ciphertext, tag = encrypt(message, key)
    binary_representation = convert_to_binary(ciphertext.hex())  # Binary representation of encrypted bytes data
    bin_length = len(binary_representation)
    write_to_yaml(key, nonce, tag, bin_length, new_yaml_location)

    # Changing the image
    change_image(path_to_image, binary_representation, path_to_new_image)

    # # Decrypting the image
    decode_image(new_yaml_location, path_to_new_image)
