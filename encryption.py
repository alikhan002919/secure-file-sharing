from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = b'ThisIsASecretKey'  # 16-byte AES key (store safely!)

def encrypt_file(data):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

def decrypt_file(enc_data):
    nonce = enc_data[:16]
    tag = enc_data[16:32]
    ciphertext = enc_data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
