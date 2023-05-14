import os
import json
from cryptography.fernet import Fernet


def decrypt_folder(encrypted_folder, key_path, decrypted_folder):
  # load the encryption key from the key file
  with open(key_path, 'rb') as f:
    key = f.read()

  cipher_suite = Fernet(key)

  # create the output folder if it doesn't exist
  if not os.path.exists(decrypted_folder):
    os.makedirs(decrypted_folder)

  # iterate over all encrypted files in the folder and decrypt them
  for root, dirs, files in os.walk(encrypted_folder):
    for file in files:
      if not file.endswith(".encrypted"):
        continue

      # read the contents of the encrypted file
      file_path = os.path.join(root, file)
      with open(file_path, 'rb') as f:
        encrypted_data = f.read()

      # decrypt the contents of the file and write it to a new file in the output folder
      decrypted_data = cipher_suite.decrypt(encrypted_data)
      decrypted_file_path = os.path.join(decrypted_folder,
                                         file.replace("." + extension, ""))
      with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)


with open('config.json', 'r') as f:
  config = json.load(f)

key_path = config['key_path']
decrypted_folder = config['decrypted_folder']
encrypted_folder = config['encrypted_folder']

decrypt_folder(encrypted_folder, key_path, decrypted_folder)
