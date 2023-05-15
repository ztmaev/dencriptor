## Encryptor/Decryptor Demo.
This project consists of two Python scripts, `encryptor.py` and `decryptor.py`, that can be used to encrypt and decrypt the contents of a folder.

## How to Use.
### 1. Install Dependencies ⬇️
  
    pip install -r requirements.txt

### 2. Configure the Scripts ⚙️
Edit the `config.json` file. Sample:
  ```json
    {
      "input_path": "input",
      "key_path": "key.txt",
      "encrypted_extension": "encr",
      "encrypted_folder": "encrypted",
      "decrypted_folder": "decrypted"    
    }
```
### 3. Encrypt the Folder 🔒

    python encryptor.py

### 4. Decrypt the Folder 🔓

    python decryptor.py
