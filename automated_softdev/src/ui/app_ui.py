import tkinter as tk
from utils.logger import get_logger
from ui.file_selector import FileSelector
class AppUI:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(__name__)
        self.root = None
        self.file_selector = None
    def initialize(self):
        self.logger.info("Inicializace uživatelského rozhraní")
        self.root = tk.Tk()
        self.root.withdraw()  # Skryjeme hlavní okno
    def show_file_selector(self, on_select, on_prompt):
        self.logger.info("Zobrazuji okno pro výběr souborů")
        self.file_selector = FileSelector(self.root, self.config.src_dir, on_select, on_prompt)
    def hide_file_selector(self):
        if self.file_selector:
            self.logger.info("Skrývám okno pro výběr souborů")
            self.file_selector.destroy()
            self.file_selector = None
    def run(self):
        self.logger.info("Spouštím hlavní smyčku UI")
        self.root.mainloop()
    def stop(self):
        self.logger.info("Ukončuji UI")
        if self.root:
            self.root.quit()
            self.root.destroy()