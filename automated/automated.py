import pyperclip
import keyboard
import time
import os
import re

# Konstanty
PROJECT_DIR = r"C:\Users\thanh\Downloads\Programy\DigitalFusion"
INCLUDE_CONFIG = True

def extract_content(project_dir, extensions):
    content = []
    src_dir = os.path.join(project_dir, 'src')
    
    if INCLUDE_CONFIG:
        for file in os.listdir(project_dir):
            if file in ['.env', '.env.local', 'package.json', 'tsconfig.json', 'next.config.js', 'next.config.mjs']:
                file_path = os.path.join(project_dir, file)
                content.extend(process_file(file_path))

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                content.extend(process_file(file_path))
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            content.append(f"Prázdná složka: {dir_path}")
    
    return "\n".join(content)

def process_file(file_path):
    content = []
    content.append(f"Obsah souboru: {file_path}")
    content.append("=" * 50)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as content_file:
            content.append(content_file.read())
    except UnicodeDecodeError:
        content.append("Nelze přečíst obsah souboru - možná binární nebo nekompatibilní kódování.")
    
    content.append("\n" + "=" * 50 + "\n")
    return content

def process_clipboard():
    clipboard_content = pyperclip.paste()
    print("Obsah schránky byl zpracován")
    print("---")

    blocks = re.findall(r'FILE_PATH:\s*(.+?)\s*<CODE_START>([\s\S]*?)<CODE_END>', clipboard_content, re.DOTALL)

    if not blocks:
        print("Chyba: Nebyly nalezeny žádné platné bloky kódu")
        return

    for file_path, code in blocks:
        file_path = file_path.strip()
        code = code.strip()

        print(f"Nalezena cesta k souboru: {file_path}")
        print("Nalezený kódový blok zpracován")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(line for line in code.splitlines() if line.strip()))

        print(f"Soubor vytvořen/upraven: {file_path}")
        print("---")

def is_processable(content):
    return 'FILE_PATH:' in content and '<CODE_START>' in content

def main():
    print("Program běží. Stiskněte Ctrl+C pro ukončení.")
    last_clipboard = ''
    
    while True:
        try:
            if keyboard.is_pressed('ctrl+shift+v'):
                print("Detekována zkratka Ctrl+Shift+V")
                extracted_content = extract_content(PROJECT_DIR, ['.tsx', '.js', '.ts', '.css', '.astro'])
                pyperclip.copy(extracted_content)
                print("Obsah extrahován a zkopírován do schránky")
                keyboard.press_and_release('ctrl+v')
                print("Obsah vložen")
                time.sleep(1)
            
            current_clipboard = pyperclip.paste()
            if current_clipboard != last_clipboard:
                print("Detekována změna ve schránce")
                if is_processable(current_clipboard):
                    print("Obsah schránky lze zpracovat, spouštím process_clipboard()")
                    process_clipboard()
                else:
                    print("Obsah schránky nelze zpracovat")
                last_clipboard = current_clipboard
            
            time.sleep(0.1)
        
        except KeyboardInterrupt:
            print("Program ukončen.")
            break

if __name__ == "__main__":
    main()