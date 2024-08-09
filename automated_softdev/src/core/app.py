import sys
import os

# Přidáme nadřazený adresář do sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import get_logger
from utils.config import Config
from core.file_manager import FileManager
from core.clipboard_manager import ClipboardManager
from core.keyboard_listener import KeyboardListener
from ui.app_ui import AppUI
from utils.api import APIClient
from code_processor import CodeProcessor
from utils.window_manager import WindowManager
from utils.repository import RepositoryMap

class App:
   def __init__(self, config):
        self.config = config
        self.logger = get_logger(__name__)
        self.file_manager = FileManager(self.config)
        self.clipboard_manager = ClipboardManager(self.config)
        self.keyboard_listener = KeyboardListener(self.config)
        self.ui = AppUI(self.config)
        self.api_client = APIClient(self.config)
        self.code_processor = CodeProcessor(self.config)
        self.window_manager = WindowManager()
        self.repository_map = RepositoryMap(self.config)

   def run(self):
       self.logger.info("Aplikace spuštěna")
       self.ui.initialize()
       self.setup_hotkeys()
       self.start_clipboard_monitoring()
       self.ui.run()

   def setup_hotkeys(self):
       self.keyboard_listener.add_hotkey('ctrl+shift+\\', self.extract_and_copy_all)
       self.keyboard_listener.add_hotkey('@', self.show_file_selector)

   def start_clipboard_monitoring(self):
       self.logger.info("Spouštím monitorování schránky")
       self.clipboard_manager.start_monitoring(self.on_clipboard_change)

   def on_clipboard_change(self, content):
       if self.code_processor.process_clipboard_content(content):
           self.logger.info("Kódové bloky zpracovány a uloženy")
       else:
           self.logger.info("Žádné kódové bloky k zpracování")

   def extract_and_copy_all(self):
       self.logger.info("Extrakce a kopírování obsahu všech souborů")
       content = self.file_manager.extract_content()
       self.clipboard_manager.set_content(content)
       self.window_manager.paste_content()
       self.logger.info("Obsah vložen")

   def show_file_selector(self):
       self.logger.info("Zobrazuji okno pro výběr souborů")
       self.ui.show_file_selector(self.on_files_selected, self.on_prompt_submitted)

   def on_files_selected(self, file_paths):
       self.logger.info(f"Vybráno souborů: {len(file_paths)}")
       content = self.file_manager.extract_content_from_files(file_paths)
       self.clipboard_manager.set_content(content)
       original_window = self.window_manager.get_foreground_window()
       self.ui.hide_file_selector()
       self.window_manager.set_foreground_window(original_window)
       self.window_manager.paste_content()
       self.logger.info("Obsah vybraných souborů vložen")

   def on_prompt_submitted(self, prompt):
        self.logger.info(f"Zpracování promptu: {prompt}")
        file_map = self.file_manager.get_file_map()
        relevant_files = self.api_client.get_relevant_files(prompt, file_map)
        
        if isinstance(relevant_files, list):
            self.logger.info(f"Nalezeno relevantních souborů: {len(relevant_files)}")
        else:
            self.logger.error("Neočekávaný formát dat z get_relevant_files")
            return

        content = self.file_manager.extract_content_from_files(relevant_files)
        content = f"PROMPT: {prompt}\n\n" + content
        self.clipboard_manager.set_content(content)
        original_window = self.window_manager.get_foreground_window()
        self.ui.hide_file_selector()
        self.window_manager.set_foreground_window(original_window)
        self.window_manager.paste_content()
        self.logger.info("Obsah relevantních souborů a prompt vložen")

   def stop(self):
       self.logger.info("Ukončuji aplikaci")
       self.keyboard_listener.stop_listening()
       self.clipboard_manager.stop_monitoring()
       self.ui.stop()

if __name__ == "__main__":
   config = Config()
   app = App(config)
   app.run()
