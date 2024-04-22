from cryptography.fernet import Fernet
import os

# Generate a key
# Define the function to encrypt a file
with open("thekey.key", "rb") as key:
    secretkey = key.read()
cipher_suite = Fernet(secretkey)

# Define the function to decrypt a file
def decrypt_file(file_path, cipher_suite):
    with open("thekey.key", 'rb') as key:
        secretkey = key.read()
    with open(file_path, 'rb') as file:
        ciphertext = file.read()
        plaintext = Fernet(secretkey).decrypt(ciphertext)
    with open(file_path, 'wb') as file:
        file.write(plaintext)

# Decrypt files in a directory and its subdirectories
def decrypt_directory(directory_path, cipher_suite):
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename == 'Ransomware.py' or filename == 'thekey.key' or filename == 'Decrypt.py':
                continue
            else:
                file_path = os.path.join(foldername, filename)
                decrypt_file(file_path, cipher_suite)

# Example usage
directory_to_protect = #'/home/dimeji/Documents/Python_Script/Temp'
#encrypt_directory(directory_to_protect, cipher_suite)

# To decrypt the files, you can use:
decrypt_directory(directory_to_protect, cipher_suite)
