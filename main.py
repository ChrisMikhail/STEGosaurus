from encryption import generate_key, encrypt, decrypt, write_to_yaml
from image import convert_to_binary, convert_to_bytes, change_image, extract_last_bit
from open_yaml import read_yaml_file


def decode_image(path_to_yaml="example/secrets.yaml", path_to_new="example/sus_steg.png"):
    """Orchestrates the decoding process"""
    example_key, example_nonce, example_tag, example_length = read_yaml_file(path_to_yaml)
    example_extracted_binary = extract_last_bit(example_length, path_to_new)
    example_decrypted_ciphertext = convert_to_bytes(example_extracted_binary)
    example_message = decrypt(example_nonce, example_decrypted_ciphertext, example_tag, example_key)
    return example_message


def encode_image(path, path_to_new, message_to_encode, yaml_location):
    """Orchestrates the encoding process"""
    # Encryption of data
    key = generate_key()  # Random AES key
    nonce, ciphertext, tag = encrypt(message_to_encode, key)
    binary_rep = convert_to_binary(ciphertext.hex())  # Binary representation of encrypted bytes data
    bin_length = len(binary_rep)
    write_to_yaml(key, nonce, tag, bin_length, yaml_location)
    # Changing the image
    change_image(path, binary_rep, path_to_new)
