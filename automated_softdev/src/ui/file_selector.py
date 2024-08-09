import tkinter as tk
from tkinter import ttk
import os
from utils.logger import get_logger

class FileSelector:
    def __init__(self, parent, directory, on_select, on_prompt):
        self.logger = get_logger(__name__)
        self.parent = parent
        self.directory = directory
        self.on_select = on_select
        self.on_prompt = on_prompt
        self.files = []
        self.filtered_files = []
        self.selected_files = set()
        self.current_index = 0

        self.window = tk.Toplevel(parent)
        self.window.title("Vybrat soubor")
        self.window.attributes('-topmost', True)

        self.search_entry = ttk.Entry(self.window, width=50)
        self.search_entry.pack(pady=5)
        self.search_entry.bind('<KeyRelease>', self.filter_files)

        self.file_listbox = tk.Listbox(self.window, height=15, width=50, selectmode=tk.MULTIPLE, activestyle='none')
        self.file_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.load_files()

        self.window.bind('<Return>', self.select_files)
        self.window.bind('<Control-Return>', self.submit_prompt)
        self.window.bind('<Escape>', self.close)
        self.window.bind('<Up>', self.move_selection)
        self.window.bind('<Down>', self.move_selection)
        self.window.bind('<Shift_L>', self.toggle_mark)
        self.window.bind('<Shift_R>', self.toggle_mark)
        self.window.bind('<space>', self.toggle_selection)
        self.window.protocol("WM_DELETE_WINDOW", self.close)

        self.window.after(100, self.focus_window)

    def load_files(self):
        self.logger.info(f"Načítám soubory z adresáře: {self.directory}")
        self.files = []
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, self.directory)
                self.files.append(rel_path)
        self.filtered_files = self.files.copy()
        self.update_file_list()

    def update_file_list(self):
        self.file_listbox.delete(0, tk.END)
        for i, file in enumerate(self.filtered_files):
            prefix = "[*]" if file in self.selected_files else "[ ]"
            self.file_listbox.insert(tk.END, f"{prefix} {file}")
            if file in self.selected_files:
                self.file_listbox.itemconfig(i, {'bg':'lightgreen'})
            elif i == self.current_index:
                self.file_listbox.itemconfig(i, {'bg':'lightblue'})
            else:
                self.file_listbox.itemconfig(i, {'bg':'white'})
        self.file_listbox.see(self.current_index)
        self.logger.info(f"Zobrazeno {len(self.filtered_files)} souborů")

    def filter_files(self, event):
        search_term = self.search_entry.get().lower()
        self.filtered_files = [f for f in self.files if search_term in f.lower()]
        self.current_index = min(self.current_index, len(self.filtered_files) - 1)
        self.update_file_list()
        self.logger.info(f"Filtrováno: {len(self.filtered_files)} souborů odpovídá vyhledávání '{search_term}'")

    def move_selection(self, event):
        if not self.filtered_files:
            return 'break'

        if event.keysym == 'Up':
            self.current_index = max(0, self.current_index - 1)
        else:  # Down
            self.current_index = min(len(self.filtered_files) - 1, self.current_index + 1)

        self.update_file_list()
        return 'break'  # Prevent default behavior

    def toggle_mark(self, event):
        if self.filtered_files:
            file = self.filtered_files[self.current_index]
            if file in self.selected_files:
                self.selected_files.remove(file)
            else:
                self.selected_files.add(file)
            self.update_file_list()
        return 'break'

    def toggle_selection(self, event):
        if self.filtered_files:
            file = self.filtered_files[self.current_index]
            if file in self.selected_files:
                self.selected_files.remove(file)
            else:
                self.selected_files.add(file)
            self.update_file_list()
        return 'break'  # Prevent default behavior

    def select_files(self, event):
        self.logger.info("Metoda select_files byla zavolána")
        if not self.selected_files and self.filtered_files:
            self.selected_files.add(self.filtered_files[self.current_index])

        if self.selected_files:
            file_paths = [os.path.join(self.directory, f) for f in self.selected_files]
            self.logger.info(f"Vybráno {len(file_paths)} souborů: {file_paths}")
            self.on_select(file_paths)
            self.close()
        else:
            self.logger.warning("Nebyly vybrány žádné soubory")

    def submit_prompt(self, event):
        prompt = self.search_entry.get()
        self.on_prompt(prompt)

    def focus_window(self):
        self.window.focus_force()
        self.search_entry.focus_set()

    def close(self, event=None):
        self.logger.info("Zavírání okna pro výběr souborů")
        self.window.destroy()

    def destroy(self):
        self.window.destroy()