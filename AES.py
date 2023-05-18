from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image


def encrypt_image(image_path, key):
    cipher = AES.new(key, AES.MODE_CBC)
    image = Image.open(image_path)
    image_data = image.tobytes()
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_data)
    encrypted_image.save('encrypted_image.png')
    print("Image encrypted successfully!")


def decrypt_image(encrypted_image_path, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_data = encrypted_image.tobytes()
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, decrypted_data)
    decrypted_image.save('decrypted_image.png')
    print("Image decrypted successfully!")


# Main program
image_path = 'image.png'  # Replace with the path to your image
key = get_random_bytes(16)  # Generate a random 128-bit (16 bytes) encryption key

print("Encryption Key:", key.hex())

encrypt_image(image_path, key)
decrypt_image('encrypted_image.png', key)
