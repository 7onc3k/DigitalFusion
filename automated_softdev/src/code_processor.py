import re
import os
from utils.logger import get_logger
from utils.api import APIClient

class CodeProcessor:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(__name__)
        self.api_client = APIClient(config)

    def process_clipboard_content(self, content):
        self.logger.info("Zpracování obsahu schránky")
        blocks = re.findall(r'FILE_PATH:\s*(.+?)\s*<CODE_START>([\s\S]*?)<CODE_END>', content, re.DOTALL)

        if not blocks:
            self.logger.warning("Nebyly nalezeny žádné platné bloky kódu")
            return False

        for file_path, code in blocks:
            self._process_code_block(file_path.strip(), code.strip())

        return True

    def _process_code_block(self, file_path, code):
        self.logger.info(f"Zpracování kódového bloku pro: {file_path}")

        # Zajistíme, že cesta k souboru je v rámci povoleného adresáře
        full_path = os.path.abspath(os.path.join(self.config.project_dir, file_path))
        if not full_path.startswith(self.config.project_dir):
            self.logger.warning(f"Pokus o vytvoření souboru mimo povolený adresář: {full_path}")
            return

        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(line for line in code.splitlines() if line.strip()))

        self.logger.info(f"Soubor vytvořen/upraven: {full_path}")

    def extract_code_blocks(self, content):
        self.logger.info("Extrakce kódových bloků")
        blocks = re.findall(r'FILE_PATH:\s*(.+?)\s*<CODE_START>([\s\S]*?)<CODE_END>', content, re.DOTALL)
        
        extracted_blocks = []
        for file_path, code in blocks:
            extracted_blocks.append({
                'file_path': file_path.strip(),
                'code': code.strip()
            })
        
        return extracted_blocks

    def create_code_block(self, file_path, code):
        return f"FILE_PATH: {file_path}\n<CODE_START>\n{code}\n<CODE_END>"