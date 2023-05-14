import os
import json
import shutil
from cryptography.fernet import Fernet


def encrypt_folder(folder_path, output_folder):
  # generate a 32-byte encryption key from the password using Fernet
  key = Fernet.generate_key()
  cipher_suite = Fernet(key)

  # create the output folder if it doesn't exist
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  # iterate over all files in the folder and encrypt them
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      # read the contents of the file
      file_path = os.path.join(root, file)
      with open(file_path, 'rb') as f:
        data = f.read()

      # encrypt the contents of the file and write it to a new file in the output folder
      encrypted_data = cipher_suite.encrypt(data)
      output_file_path = os.path.join(output_folder, file + "." + extension)
      with open(output_file_path, 'wb') as f:
        f.write(encrypted_data)

  # write the encryption key to a file in the output folder for later use
  with open(os.path.join(key_path), 'wb') as f:
    f.write(key)


with open('config.json', 'r') as f:
  config = json.load(f)

input_path = config['input_path']
encrypted_folder = config['encrypted_folder']
extension = config['encrypted_extension']
key_path = config['key_path']
encrypt_folder(input_path, encrypted_folder)
