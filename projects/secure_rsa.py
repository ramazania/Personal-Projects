from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt(plaintext, pub_key):
    key = RSA.import_key(pub_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def decrypt(ciphertext, priv_key):
    key = RSA.import_key(priv_key)
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(ciphertext).decode()
    return plaintext

if __name__ == '__main__':
    private_key, public_key = generate_keypair()
    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(message, public_key)
    print("Encrypted message: ", encrypted_msg)
    decrypted_msg = decrypt(encrypted_msg, private_key)
    print("Decrypted message: ", decrypted_msg)
