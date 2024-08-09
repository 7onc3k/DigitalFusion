from utils.logger import get_logger

logger = get_logger(__name__)

async def process_file(session, api_client, file_path, rel_path, map_dict):
    try:
        file_content = read_file_content(file_path)
        file_description = await api_client.analyze_file_content_async(session, file_content)
        if isinstance(file_description, dict) and 'error' not in file_description:
            # Použijeme normalizovanou cestu jako klíč
            map_dict[rel_path] = file_description
            print(f"Přidán popis pro soubor: {rel_path}")
            logger.info(f"Přidán popis pro soubor: {rel_path}")
        else:
            print(f"Chyba při zpracování souboru {rel_path}: Neplatná odpověď API")
            logger.error(f"Chyba při zpracování souboru {rel_path}: Neplatná odpověď API")
    except Exception as e:
        print(f"Chyba při zpracování souboru {rel_path}: {str(e)}")
        logger.error(f"Chyba při zpracování souboru {rel_path}: {str(e)}")

def read_file_content(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"Úspěšně přečten obsah souboru: {file_path}")
        logger.info(f"Úspěšně přečten obsah souboru: {file_path}")
        return content
    except Exception as e:
        print(f"Chyba při čtení souboru {file_path}: {str(e)}")
        logger.error(f"Chyba při čtení souboru {file_path}: {str(e)}")
        raise