import aiohttp
import requests
import json
from utils.logger import get_logger
from .request_builder import create_api_request_data
from .response_parser import parse_api_response

class APIClient:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(__name__)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config.deepseek_api_key}"
        }
        self.logger.info(f"APIClient inicializován s URL: {self.config.deepseek_api_url}")
        self.logger.info(f"Použitý API klíč (prvních 5 znaků): {self.config.deepseek_api_key[:5]}...")

    async def analyze_file_content_async(self, session, file_content):
        self.logger.info("Začínám asynchronní analýzu souboru")
        prompt = self._create_analysis_prompt(file_content)
        data = create_api_request_data(prompt)
        
        try:
            async with session.post(self.config.deepseek_api_url, headers=self.headers, json=data, timeout=30) as response:
                self.logger.info(f"Obdržena odpověď od API. Status: {response.status}")
                response.raise_for_status()
                result = await response.text()
                self.logger.debug(f"Surová odpověď API: {result}")
                
                parsed_content = parse_api_response(result)
                if parsed_content:
                    self.logger.info(f"Úspěšně zpracovaný obsah: {parsed_content}")
                    return parsed_content
                else:
                    self.logger.error("Nepodařilo se zpracovat odpověď API")
                    return {"error": "Došlo k chybě při analýze souboru"}
        except aiohttp.ClientError as e:
            self.logger.error(f"Chyba při HTTP požadavku: {str(e)}")
        except Exception as e:
            self.logger.error(f"Neočekávaná chyba při asynchronní analýze souboru: {str(e)}")
        
        return {"error": "Došlo k chybě při analýze souboru"}

    def analyze_file_content(self, file_content):
        self.logger.info("Začínám synchronní analýzu souboru")
        prompt = self._create_analysis_prompt(file_content)
        data = create_api_request_data(prompt)
        
        try:
            response = requests.post(self.config.deepseek_api_url, headers=self.headers, json=data, timeout=30)
            self.logger.info(f"Obdržena odpověď od API. Status: {response.status_code}")
            response.raise_for_status()
            result = response.text
            self.logger.debug(f"Surová odpověď API: {result}")
            
            parsed_content = parse_api_response(result)
            if parsed_content:
                self.logger.info(f"Úspěšně zpracovaný obsah: {parsed_content}")
                return parsed_content
            else:
                self.logger.error("Nepodařilo se zpracovat odpověď API")
                return {"error": "Došlo k chybě při analýze souboru"}
        except requests.RequestException as e:
            self.logger.error(f"Chyba při HTTP požadavku: {str(e)}")
        except Exception as e:
            self.logger.error(f"Neočekávaná chyba při synchronní analýze souboru: {str(e)}")
        
        return {"error": "Došlo k chybě při analýze souboru"}

    def get_relevant_files(self, prompt, file_map):
        self.logger.info("Získávám relevantní soubory z Deepseek API")
        query = self._create_relevance_query(prompt, file_map)
        data = create_api_request_data(query)
        
        try:
            response = requests.post(self.config.deepseek_api_url, headers=self.headers, json=data, timeout=30)
            self.logger.info(f"Obdržena odpověď od API. Status: {response.status_code}")
            response.raise_for_status()
            result = response.text
            self.logger.debug(f"Surová odpověď API pro relevantní soubory: {result}")
            
            parsed_content = parse_api_response(result)
            if parsed_content and isinstance(parsed_content, dict) and 'relevant_files' in parsed_content:
                relevant_files = parsed_content['relevant_files']
                self.logger.info(f"Úspěšně zpracovaný obsah pro relevantní soubory: {relevant_files}")
                return relevant_files
            else:
                self.logger.error("Nepodařilo se zpracovat odpověď API pro relevantní soubory")
                return []
        except requests.RequestException as e:
            self.logger.error(f"Chyba při HTTP požadavku pro relevantní soubory: {str(e)}")
        except Exception as e:
            self.logger.error(f"Neočekávaná chyba při získávání relevantních souborů: {str(e)}")
        
        return []

    def _create_analysis_prompt(self, file_content):
        return f'''Analyze the following code and provide a structured description in JSON format:
        {{
          "type": "File type",
          "description": "Short explanation of purpose",
          "exports": ["list of exports"],
          "imports": ["list of imports"],
          "functions": ["key functions with short descriptions"],
          "hooks": ["used hooks"],
          "attributes": ["characteristics"],
          "category": "file category"
        }}

        Code:
        {file_content[:100]}...  # Logging only first 100 characters to avoid clutter
        '''

    def _create_relevance_query(self, prompt, file_map):
        return f'''Based on the following file map and user prompt, identify and list the paths of the most relevant files:
        File Map:
        {json.dumps(file_map, ensure_ascii=False)}
        User Prompt:
        {prompt}
        Please return only a JSON array of file paths, like this:
        ["path/to/file1.js", "path/to/file2.tsx"]
        '''
