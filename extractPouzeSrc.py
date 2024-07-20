import os
import pyperclip

# Zde nastavte True pro zahrnutí konfiguračních souborů, False pro jejich vynechání
INCLUDE_CONFIG = True

def extract_content(root_dir, extensions):
    content = []
    src_dir = os.path.join(root_dir, 'src')
    
    # Zpracování konfiguračních souborů v kořenovém adresáři
    if INCLUDE_CONFIG:
        for file in os.listdir(root_dir):
            if file in ['.env', '.env.local' 'package.json', 'tsconfig.json', 'next.config.js', 'next.config.mjs', ]:
                file_path = os.path.join(root_dir, file)
                content.extend(process_file(file_path))

    # Zpracování ostatních souborů ve složce src
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                content.extend(process_file(file_path))
    
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

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    extensions = ['.tsx', '.js', '.ts', '.css', '.astro']
    output_file = "extracted_content.txt"
    
    extracted_content = extract_content(current_dir, extensions)
    
    # Uložení do souboru
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(extracted_content)
    
    # Kopírování do schránky
    pyperclip.copy(extracted_content)
    
    print(f"Extrakce dokončena. Obsah byl uložen do souboru {output_file} a zkopírován do schránky.")
    print(f"Konfigurační soubory byly {'zahrnuty' if INCLUDE_CONFIG else 'vynechány'}.")