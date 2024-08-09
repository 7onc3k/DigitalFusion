import os
import sys
import json
import asyncio
import aiohttp
from typing import List, Dict

# Přidáme cestu k src adresáři do sys.path
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(current_dir)

from utils.logger import get_logger, setup_logger
from utils.config import Config
from utils.api.client import APIClient
from utils.repository.file_processor import process_file, read_file_content
from utils.repository.git_utils import get_changed_files

logger = get_logger(__name__)

class RepositoryMap:
    def __init__(self, config: Config):
        self.config = config
        self.api_client = APIClient(config)
        self.map_file = self.config.repository_map_file
        print(f"RepositoryMap inicializován, map_file: {self.map_file}")
        print(f"Config: {self.config}")

    async def update_map(self):
        print("Aktualizace repository map zahájena")
        logger.info("Aktualizace repository map zahájena")

        current_map = self._load_current_map()
        if not current_map:
            print("Vytváření počáteční mapy repozitáře")
            logger.info("Vytváření počáteční mapy repozitáře")
            await self._create_initial_map()
        else:
            changed_files = await get_changed_files(self.config.project_dir)
            print(f"Změněné soubory: {changed_files}")
            if changed_files:
                updated_map = await self._process_changed_files(changed_files, current_map)
                self._save_map(updated_map)
            else:
                print("Žádné změny k aktualizaci")
                logger.info("Žádné změny k aktualizaci")

        print("Aktualizace repository map dokončena")
        logger.info("Aktualizace repository map dokončena")

    async def _create_initial_map(self):
        initial_map = {}
        tasks = []
        async with aiohttp.ClientSession() as session:
            for root, _, files in os.walk(self.config.src_dir):
                for file in files:
                    if any(file.endswith(ext) for ext in self.config.file_extensions):
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, self.config.project_dir)
                        # Normalizujeme cestu
                        normalized_path = os.path.normpath(rel_path).replace(os.sep, '/')
                        tasks.append(process_file(session, self.api_client, file_path, normalized_path, initial_map))
            await asyncio.gather(*tasks)
        self._save_map(initial_map)

    async def _process_changed_files(self, changed_files: List[str], current_map: Dict) -> Dict:
        async with aiohttp.ClientSession() as session:
            tasks = []
            for file_path in changed_files:
                if file_path.startswith('src/'):
                    # Normalizujeme cestu
                    normalized_path = os.path.normpath(file_path).replace(os.sep, '/')
                    full_path = os.path.join(self.config.project_dir, file_path)
                    if os.path.exists(full_path) and any(file_path.endswith(ext) for ext in self.config.file_extensions):
                        tasks.append(process_file(session, self.api_client, full_path, normalized_path, current_map))
                    elif normalized_path in current_map:
                        del current_map[normalized_path]
                        print(f"Odstraněn popis pro smazaný soubor: {normalized_path}")
                        logger.info(f"Odstraněn popis pro smazaný soubor: {normalized_path}")
            await asyncio.gather(*tasks)
        return current_map

    def _load_current_map(self) -> Dict:
        if os.path.exists(self.map_file):
            try:
                with open(self.map_file, 'r', encoding='utf-8') as f:
                    current_map = json.load(f)
                if current_map:
                    return current_map
                else:
                    print("Existující mapa je prázdná. Bude vytvořena nová.")
                    logger.info("Existující mapa je prázdná. Bude vytvořena nová.")
                    return {}
            except json.JSONDecodeError as e:
                print(f"Chyba při čtení repository_map.json: {str(e)}")
                logger.error(f"Chyba při čtení repository_map.json: {str(e)}")
                print("Vytvářím novou mapu repozitáře.")
                logger.info("Vytvářím novou mapu repozitáře.")
                return {}
        else:
            print("Soubor repository_map.json neexistuje. Vytvářím novou mapu repozitáře.")
            logger.info("Soubor repository_map.json neexistuje. Vytvářím novou mapu repozitáře.")
            return {}

    def _save_map(self, map_data: Dict):
        try:
            with open(self.map_file, 'w', encoding='utf-8') as f:
                json.dump(map_data, f, ensure_ascii=False, indent=2)
            print(f"Repository map úspěšně uložena do {self.map_file}")
            logger.info(f"Repository map úspěšně uložena do {self.map_file}")
        except Exception as e:
            print(f"Chyba při ukládání mapy do {self.map_file}: {str(e)}")
            logger.error(f"Chyba při ukládání mapy do {self.map_file}: {str(e)}")

async def update_repository_map(config: Config):
    repo_map = RepositoryMap(config)
    await repo_map.update_map()

if __name__ == "__main__":
    print("Skript repository_map.py spuštěn")
    try:
        config = Config()
        setup_logger(config.log_level)
        asyncio.run(update_repository_map(config))
    except Exception as e:
        print(f"Došlo k neočekávané chybě: {str(e)}")
        import traceback
        print(traceback.format_exc())