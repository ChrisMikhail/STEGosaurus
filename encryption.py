from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def generate_key():
    """Generates a random 16 byte key"""
    return get_random_bytes(16)


def encrypt(message, key):
    """Encrypts the message before encrypting it in an image"""
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag, key):
    """Decrypt the ciphertext"""
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode('utf-8')
    except ValueError:
        return None
    