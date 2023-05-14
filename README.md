<h2>Encryptor/Decryptor Demo.</h2>
This project consists of two Python scripts, encryptor.py and decryptor.py, that can be used to encrypt and decrypt the contents of a folder.

<h2>How to Use.</h2>
<h3>1. Install Dependencies</h3>
  
    pip install -r requirements.txt

<h3><strong>2. Configure the Scripts<strong><h3>
<p>Edit the <strong>config.json</strong> file.<p>Sample
  
    {
      "input_path": "input",
      "key_path": "key.txt",
      "encrypted_extension": "encr",
      "encrypted_folder": "encrypted",
      "decrypted_folder": "decrypted"    
    }
<h3>3. Encrypt the Folder</h3>

    python encryptor.py

<h3>4. Decrypt the Folder</h3>

    python decryptor.py
    
