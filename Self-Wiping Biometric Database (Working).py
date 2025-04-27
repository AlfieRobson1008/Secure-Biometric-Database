import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import shutil
import time

# Paths to encrypted/ decrypted folders
GENERATED_IMAGES_PATH = "generated_images/"
ENCRYPTED_IMAGES_PATH = "encrypted_images/"
DECRYPTED_IMAGES_PATH = "decrypted_images/"
BACKUP_PATH = "backup/"
KEY_FILE = "encryption_key.key"

#Credentials required for login
USERNAME = "BioAdmin"
PASSWORD = "BioAdmin1"

# Generate and save encryption key securely
# This function should be called only once to generate the key
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        print("Encryption key generated and saved.")

# Load encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        raise Exception("Encryption key not found. Please generate the key first.")
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

# Image encryption process
def encrypt_images():
    os.makedirs(ENCRYPTED_IMAGES_PATH, exist_ok=True)
    key = load_key()
    fernet = Fernet(key)

    for image_file in os.listdir(GENERATED_IMAGES_PATH):
        original_path = os.path.join(GENERATED_IMAGES_PATH, image_file)
        encrypted_path = os.path.join(ENCRYPTED_IMAGES_PATH, f"{image_file}.enc")

        with open(original_path, "rb") as file:
            image_data = file.read()
        encrypted_data = fernet.encrypt(image_data)

        with open(encrypted_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        print(f"Encrypted: {original_path} -> {encrypted_path}")

    messagebox.showinfo("Encryption Completed", "All images have been encrypted.")

# Decryption process for viewing gallery
def decrypt_images():
    os.makedirs(DECRYPTED_IMAGES_PATH, exist_ok=True)
    key = load_key()
    fernet = Fernet(key)

    for encrypted_file in os.listdir(ENCRYPTED_IMAGES_PATH):
        encrypted_path = os.path.join(ENCRYPTED_IMAGES_PATH, encrypted_file)
        decrypted_path = os.path.join(DECRYPTED_IMAGES_PATH, encrypted_file.replace(".enc", ""))

        with open(encrypted_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(decrypted_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        print(f"Decrypted: {encrypted_path} -> {decrypted_path}")

# Data backup process to prevent loss of data
def backup_data():
    os.makedirs(BACKUP_PATH, exist_ok=True)

    # Backup 'generated_images'
    backup_folder("generated_images")
    # Backup 'encrypted_images'
    backup_folder("encrypted_images")
    # Backup 'decrypted_images'
    backup_folder("decrypted_images")

def backup_folder(folder_name):
    source_folder = os.path.join(folder_name)
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Unique timestamp for backup
    target_folder = os.path.join(BACKUP_PATH, f"{folder_name}_{timestamp}")
    
    if os.path.exists(source_folder):
        shutil.copytree(source_folder, target_folder)
        print(f"Backup created for {folder_name} -> {target_folder}")
    else:
        print(f"No files found in {source_folder} to backup.")

# Database wiping process, using simulated breach funtion
def wipe_database():
    wipe_folder("generated_images")
    wipe_folder("encrypted_images")
    wipe_folder("decrypted_images")

def wipe_folder(folder_name):
    folder_path = os.path.join(folder_name)
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
        print(f"Wiped all files from {folder_name}")
    else:
        print(f"No files found in {folder_name} to wipe.")

# Main Application
class SyntheticFaceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Biometric Database System")
        self.geometry("600x500")
        self.configure(bg="#ADD8E6")  # Light blue background for professionality and simplicity

        self.show_login_screen()
# Login page with a username and password authentication system
    def show_login_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Login", font=("Arial", 24, "bold"), bg="#ADD8E6", fg="#003366").pack(pady=30)
        tk.Label(self, text="Username:", bg="#ADD8E6", font=("Arial", 14)).pack()
        self.username_entry = tk.Entry(self, font=("Arial", 12))
        self.username_entry.pack(pady=10)

        tk.Label(self, text="Password:", bg="#ADD8E6", font=("Arial", 14)).pack()
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=10)

        tk.Button(self, text="Login", command=self.check_credentials, bg="#005F99", fg="white", font=("Arial", 12), bd=0, padx=20, pady=5).pack(pady=20)
# credentials are checked against the hardcoded username and password
    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == USERNAME and password == PASSWORD:
            messagebox.showinfo("Login Successful", "Welcome, BioAdmin!")
            self.show_database_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def show_database_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
# Display of Main Menu and its functions
        tk.Label(self, text="Database Interface", font=("Arial", 24, "bold"), bg="#ADD8E6", fg="#003366").pack(pady=30)
        tk.Button(
            self, text="Encrypt Images", command=encrypt_images,
            bg="#007ACC", fg="white", font=("Arial", 14), bd=0, padx=20, pady=5
        ).pack(pady=10)
        tk.Button(
            self, text="Decrypt Images and View Gallery", command=self.view_database,
            bg="#007ACC", fg="white", font=("Arial", 14), bd=0, padx=20, pady=5
        ).pack(pady=10)
        tk.Button(
            self, text="Simulate Breach", command=self.simulate_breach,
            bg="red", fg="white", font=("Arial", 14), bd=0, padx=20, pady=5
        ).pack(pady=10)
        tk.Button(
            self, text="Exit", command=self.destroy,
            bg="#005F99", fg="white", font=("Arial", 14), bd=0, padx=20, pady=5
        ).pack(pady=10)
# Display process of the Biometric Image Gallery
    def view_database(self):
        decrypt_images()

        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Biometric Image Gallery", font=("Arial", 24, "bold"), bg="#ADD8E6", fg="#003366").pack(pady=30)

        self.images = [os.path.join(DECRYPTED_IMAGES_PATH, img) for img in os.listdir(DECRYPTED_IMAGES_PATH)]
        if not self.images:
            tk.Label(self, text="No images found!", bg="#ADD8E6", fg="red", font=("Arial", 14)).pack(pady=20)
        else:
            self.current_image_index = 0
            self.img_label = tk.Label(self, bg="#ADD8E6")  # Placeholder for the image
            self.img_label.pack(pady=20)

            # Navigation buttons for user to navigate through the images
            nav_frame = tk.Frame(self, bg="#ADD8E6")
            nav_frame.pack(pady=10)

            tk.Button(nav_frame, text="<< Previous", command=self.previous_image,
                      bg="#005F99", fg="white", font=("Arial", 12), bd=0).pack(side=tk.LEFT, padx=10)
            tk.Button(nav_frame, text="Next >>", command=self.next_image,
                      bg="#007ACC", fg="white", font=("Arial", 12), bd=0).pack(side=tk.LEFT, padx=10)

            self.display_image()  # Display the first image

        tk.Button(
            self, text="Back to Menu", command=self.show_database_screen,
            bg="#005F99", fg="white", font=("Arial", 14), bd=0, padx=20, pady=5
        ).pack(pady=20)

    def display_image(self):
        # Clear the previous image if it exists
        if hasattr(self, "img_label"):
            self.img_label.config(image="")  # Clear the image

        img_path = self.images[self.current_image_index]
        img = Image.open(img_path)
        img = img.resize((400, 400), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing
        photo = ImageTk.PhotoImage(img)

        self.img_label.config(image=photo)
        self.img_label.image = photo  

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.display_image()

    def previous_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.images)
        self.display_image()

    def simulate_breach(self):
        backup_data()
        wipe_database()
        messagebox.showinfo("Simulate Breach", "Data backed up and original database wiped successfully.")

if __name__ == "__main__":
    app = SyntheticFaceApp()
    app.mainloop()