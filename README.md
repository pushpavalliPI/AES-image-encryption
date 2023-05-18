Python program that uses the PyCryptodome library to encrypt and decrypt an image using the AES (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining) mode. The program will also display the encryption key used.
First, make sure you have the Pillow library installed, which is a fork of the Python Imaging Library (PIL), and the pycryptodome library.

How it works:
1. We import the necessary libraries: `Crypto.Cipher` from `pycryptodome` for AES encryption, `Crypto.Random` for generating random encryption keys, `Crypto.Util.Padding` for adding padding to the image data, and `PIL.Image` from `Pillow` for image manipulation.
2. The `encrypt_image` function takes an image path and an encryption key as inputs. It opens the image using PIL, converts it to bytes, and encrypts the data using AES in CBC mode. The encrypted data is then saved as a new image.
3. The `decrypt_image` function takes the path of the encrypted image and the encryption key as inputs. It opens the encrypted image using PIL, decrypts the image data using AES in CBC mode, removes the padding, and saves the decrypted image.
4. In the main program, we specify the path to the image you want to encrypt (`image_path`), and generate a random 128-bit encryption key (`key`) using `get_random_bytes` from `Crypto.Random`.
5. The encryption key is displayed in hexadecimal format using `key.hex()`.
6. The `encrypt_image` function is called with the image path and encryption key, which encrypts the image and saves it as `encrypted_image.png`.
7. The `decrypt_image` function is called with the path of the encrypted image and the encryption key, which decrypts the image and saves it as `decrypted_image.png`.

Note: Make sure the image you want to encrypt is in the same directory as the Python script, or you can provide the full path to the image file.

This code demonstrates a basic implementation of image encryption and decryption using the AES algorithm in CBC mode. AES is a symmetric encryption algorithm that operates
