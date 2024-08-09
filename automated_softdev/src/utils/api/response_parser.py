import json
from utils.logger import get_logger

logger = get_logger(__name__)

def parse_api_response(response_text):
    logger.debug(f"Surová odpověď API: {response_text[:1000]}...")
    try:
        result_json = json.loads(response_text)
        logger.debug(f"Parsovaný JSON: {result_json}")
        
        if 'choices' not in result_json or not result_json['choices']:
            raise KeyError("Chybí klíč 'choices' v odpovědi API")
        
        content = result_json['choices'][0]['message']['content']
        logger.debug(f"Extrahovaný obsah: {content}")
        
        parsed_content = json.loads(content)
        return parsed_content
    except json.JSONDecodeError as e:
        logger.error(f"Chyba při parsování JSON: {str(e)}")
        logger.error(f"Problematická odpověď: {response_text}")
    except KeyError as e:
        logger.error(f"Chyba při přístupu k datům v odpovědi: {str(e)}")
        logger.error(f"Struktura odpovědi: {result_json}")
    except Exception as e:
        logger.error(f"Neočekávaná chyba při zpracování odpovědi API: {str(e)}")
    
    return None
