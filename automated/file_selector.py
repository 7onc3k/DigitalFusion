import tkinter as tk
import os
from utils import set_foreground_window

class FileSelector:
    def __init__(self, parent, directory, on_select, on_close):
        self.parent = parent
        self.directory = directory
        self.on_select = on_select
        self.on_close = on_close
        self.current_selection = 0
        self.files = []
        self.marked_files = set()
        self.filtered_files = []

        self.window = tk.Toplevel(parent)
        self.window.title("Select File")
        self.window.attributes('-topmost', True)

        self.file_listbox = tk.Listbox(self.window, height=15, width=50, selectmode=tk.SINGLE)
        self.file_listbox.pack(pady=10)

        self.search_entry = tk.Entry(self.window, width=50)
        self.search_entry.pack(pady=5)
        self.search_entry.bind('<KeyRelease>', self.filter_files)

        self.load_files()

        self.window.bind('<Return>', self.select_files)
        self.window.bind('<Up>', self.move_selection)
        self.window.bind('<Down>', self.move_selection)
        self.window.bind('<Shift_R>', self.toggle_mark)  # Změněno z '<space>' na '<Shift_R>'
        self.window.bind('<Escape>', self.on_close)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Přidáno: zachytávání všech kláves na úrovni okna
        self.window.bind('<Key>', self.handle_key)

        self.window.after(100, self.focus_window)

    def handle_key(self, event):
        # Pokud je stisknut pravý Shift, zavoláme toggle_mark a zabráníme dalšímu zpracování
        if event.keysym == 'Shift_R':  # Změněno z event.char == ' ' na event.keysym == 'Shift_R'
            self.toggle_mark(event)
            return 'break'
        # Pro ostatní klávesy necháme událost propagovat dál
        return None

    def focus_window(self):
        self.window.focus_force()
        self.search_entry.focus_set()
        if os.name == 'nt':
            set_foreground_window(self.window.winfo_id())

    def load_files(self):
        print(f"Načítám soubory z adresáře: {self.directory}")
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
        for file in self.filtered_files:
            if file in self.marked_files:
                self.file_listbox.insert(tk.END, f"[*] {file}")
            else:
                self.file_listbox.insert(tk.END, f"[ ] {file}")
        print(f"Zobrazeno {len(self.filtered_files)} souborů")
        self.update_selection()

    def update_selection(self):
        if self.filtered_files:
            self.file_listbox.selection_clear(0, tk.END)
            self.file_listbox.selection_set(self.current_selection)
            self.file_listbox.see(self.current_selection)

    def filter_files(self, event):
        search_term = self.search_entry.get().lower()
        self.filtered_files = [f for f in self.files if search_term in f.lower() or f in self.marked_files]
        self.update_file_list()
        print(f"Filtrováno: {len(self.filtered_files)} souborů odpovídá vyhledávání '{search_term}'")

    def move_selection(self, event):
        if not self.filtered_files:
            return

        if event.keysym == 'Up':
            self.current_selection = max(0, self.current_selection - 1)
        elif event.keysym == 'Down':
            self.current_selection = min(len(self.filtered_files) - 1, self.current_selection + 1)

        self.update_selection()
        return 'break'

    def toggle_mark(self, event):
        if self.filtered_files:
            selected_file = self.filtered_files[self.current_selection]
            if selected_file in self.marked_files:
                self.marked_files.remove(selected_file)
            else:
                self.marked_files.add(selected_file)
            self.update_file_list()

    def select_files(self, event):
        selected_files = list(self.marked_files)
        if self.filtered_files:
            current_file = self.filtered_files[self.current_selection]
            if current_file not in selected_files:
                selected_files.append(current_file)
        
        if selected_files:
            file_paths = [os.path.join(self.directory, f) for f in selected_files]
            self.on_select(file_paths)

    def destroy(self):
        self.window.destroy()