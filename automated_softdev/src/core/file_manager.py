import os
from utils.logger import get_logger

class FileManager:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(__name__)

    def extract_content(self):
        content = []
        self.logger.info(f"Extrahování obsahu z {self.config.project_dir}")
        
        # Zpracování konfiguračních souborů z kořenového adresáře
        if self.config.include_config_files:
            content.extend(self._process_config_files())
        
        # Zpracování souborů v src adresáři
        for root, dirs, files in os.walk(self.config.src_dir):
            for file in files:
                if any(file.endswith(ext) for ext in self.config.file_extensions):
                    file_path = os.path.join(root, file)
                    content.extend(self._process_file(file_path))
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                content.append(f"Prázdná složka: {dir_path}")
        return "\n".join(content)
    
    def extract_content_from_files(self, file_paths):
        content = []
        self.logger.info(f"Extrahování obsahu z vybraných souborů")
        for file_path in file_paths:
            full_path = os.path.join(self.config.project_dir, file_path)
            if os.path.exists(full_path):
                content.extend(self._process_file(full_path))
            else:
                self.logger.warning(f"Soubor nenalezen: {full_path}")
        return "\n".join(content)
    
    def get_file_map(self):
        file_map = {}
        self.logger.info(f"Vytváření mapy souborů z {self.config.project_dir}")
        
        # Přidání konfiguračních souborů do mapy
        if self.config.include_config_files:
            for file in self.config.config_files:
                file_path = os.path.join(self.config.project_dir, file)
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_map[file] = f.read()
        
        # Přidání souborů ze src adresáře do mapy
        for root, _, files in os.walk(self.config.src_dir):
            for file in files:
                if any(file.endswith(ext) for ext in self.config.file_extensions):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.config.project_dir)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_map[rel_path] = f.read()
        return file_map

    def _process_config_files(self):
        content = []
        for file in self.config.config_files:
            file_path = os.path.join(self.config.project_dir, file)
            if os.path.exists(file_path):
                content.extend(self._process_file(file_path))
        return content

    def _process_file(self, file_path):
        content = []
        self.logger.info(f"Zpracování souboru: {file_path}")
        content.append(f"Obsah souboru: {file_path}")
        content.append("=" * 50)
        try:
            with open(file_path, 'r', encoding='utf-8') as content_file:
                content.append(content_file.read())
        except UnicodeDecodeError:
            content.append("Nelze přečíst obsah souboru - možná binární nebo nekompatibilní kódování.")
        content.append("\n" + "=" * 50 + "\n")
        return content
