import pyperclip
import os
import re

def process_clipboard():
    # Získání obsahu schránky
    clipboard_content = pyperclip.paste()
    print("Obsah schránky:")
    print(clipboard_content)
    print("---")

    # Hledání všech bloků kódu s použitím méně striktního vzoru
    blocks = re.findall(r'FILE_PATH:\s*(.+?)\s*<CODE_START>([\s\S]*?)<CODE_END>', clipboard_content, re.DOTALL)

    if not blocks:
        print("Chyba: Nebyly nalezeny žádné platné bloky kódu")
        return

    for file_path, code in blocks:
        file_path = file_path.strip()
        code = code.strip()

        print(f"Nalezena cesta k souboru: {file_path}")
        print("Nalezený kódový blok:")
        print(code)

        # Vytvoření adresářů, pokud neexistují
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Zápis nebo přepsání souboru bez přidávání prázdných řádků
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(line for line in code.splitlines() if line.strip()))

        print(f"Soubor vytvořen/upraven: {file_path}")
        
        # Vypíše obsah zapsaného souboru pro kontrolu
        print("Obsah zapsaného souboru:")
        with open(file_path, 'r', encoding='utf-8') as file:
            print(file.read())
        
        print("---")

if __name__ == "__main__":
    process_clipboard()