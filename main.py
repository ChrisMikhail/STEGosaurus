from encryption import generate_key, encrypt, decrypt
from image import get_image_object, convert_to_binary, convert_to_bytes, change_image, extract_last_bit
from open_yaml import read_yaml_file


def hello_word():
    input(
        "Hello, there! The original image is in the static folder and is named steg and the secret message is in "
        "sus_steg. Press any key to see what the message!")
    example_secrets = (read_yaml_file())["example"]
    example_key = eval(example_secrets["key"].encode('utf-8'))
    example_nonce = eval(example_secrets["nonce"].encode('utf-8'))
    example_tag = eval(example_secrets["tag"].encode('utf-8'))
    example_length = int(example_secrets["length"])
    example_extracted_binary = extract_last_bit(example_length)
    example_decrypted_ciphertext = convert_to_bytes(example_extracted_binary)
    example_message = decrypt(example_nonce, example_decrypted_ciphertext, example_tag, example_key)
    print(f"The image contained the message {example_message}\n")


def introduce_program():
    """Introduces program and gets path to image and message to encrypt from user."""
    image_name = input("Welcome to STEGosaurus! Enter the name of your image in the static folder to get started ("
                       "Don't include file extension): ")
    name_of_new_image = input("Enter the name of your new image, it will be saved in the static folder of this "
                              "project: ")
    message_to_encode = input("Now, enter a message to hide in the image: ")
    return image_name, name_of_new_image, message_to_encode


if __name__ == '__main__':
    hello_word()
    # Unpack basic data
    name_of_image, new_image_name, message = introduce_program()
    path_to_image = f"static/{name_of_image}.png"  # Original image path
    path_to_new_image = f"static/{new_image_name}.png"  # Path for new image
    image_object = get_image_object(path_to_image)  # Generates a PIL image object

    # Encryption of data
    key = generate_key()  # Random AES key
    nonce, ciphertext, tag = encrypt(message, key)
    binary_representation = convert_to_binary(ciphertext.hex())  # Binary representation of encrypted bytes data

    # Changing the image
    change_image(path_to_image, binary_representation, new_image_name)

    # Decrypting the image
    decrypted_binary = extract_last_bit(len(binary_representation), f"static/{new_image_name}.png")
    decrypted_ciphertext = convert_to_bytes(decrypted_binary)
    message = decrypt(nonce, decrypted_ciphertext, tag, key)
    print("Your message was: " + message)
