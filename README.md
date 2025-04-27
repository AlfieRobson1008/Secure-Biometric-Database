# Self-Wiping Biometric Database

This project is a biometric database system that allows users to encrypt, decrypt, and view images securely. It also includes functionality to simulate a data breach by backing up and wiping the database.

## Features

- **Encryption**: Encrypt biometric images for secure storage.
- **Decryption**: Decrypt images for viewing in a gallery.
- **Backup**: Create backups of the database to prevent data loss.
- **Simulated Breach**: Backup and wipe the database to simulate a security breach.
- **User Authentication**: Login system with hardcoded credentials.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or later
- Required Python libraries:
  - `tkinter`
  - `Pillow`
  - `cryptography`

You can install the required libraries using the following command:

```bash
pip install pillow cryptography


Ensure the following folder structure exists in the project directory:

generated_images: Place images to be encrypted here.
encrypted_images: Encrypted images will be stored here.
decrypted_images: Decrypted images will be stored here.
backup: Backups will be stored here.

In Terminal, Enter:
python "Self-Wiping Biometric Database (Working).py"

Usage
Login: Use the following credentials to log in:

Username: BioAdmin
Password: BioAdmin1
Encrypt Images:

Place images in the generated_images folder.
Click the "Encrypt Images" button to encrypt them. Encrypted files will be saved in the encrypted_images folder.
Decrypt Images and View Gallery:

Click the "Decrypt Images and View Gallery" button to decrypt images and view them in a gallery.
Simulate Breach:

Click the "Simulate Breach" button to back up the database and wipe all data from the generated_images, encrypted_images, and decrypted_images folders.
Exit:

Click the "Exit" button to close the application.

