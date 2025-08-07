from cryptography.fernet import Fernet

def generate_key():
    """Generate and save AES key."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key.")

def load_key():
    """Load saved AES key."""
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    """Encrypt file content."""
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)
    print(f"File encrypted: {filename}.enc")

def decrypt_file(filename, key):
    """Decrypt file content."""
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted = f.decrypt(encrypted_data)
    output_file = filename.replace(".enc", ".dec")
    with open(output_file, "wb") as file:
        file.write(decrypted)
    print(f"File decrypted: {output_file}")

if __name__ == "__main__":
    print("1: Generate key\n2: Encrypt file\n3: Decrypt file")
    choice = input("Choose option: ")
    if choice == "1":
        generate_key()
    elif choice == "2":
        file_to_encrypt = input("Enter file to encrypt: ")
        key = load_key()
        encrypt_file(file_to_encrypt, key)
    elif choice == "3":
        file_to_decrypt = input("Enter file to decrypt: ")
        key = load_key()
        decrypt_file(file_to_decrypt, key)
