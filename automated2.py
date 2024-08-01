import tkinter as tk
import os
from pynput import keyboard
from pynput.keyboard import Key, Controller
import threading
import pyperclip
import ctypes

def set_foreground_window(window_handle):
    if os.name == 'nt':
        ctypes.windll.user32.SetForegroundWindow(window_handle)

class FileInsertApp:
    def __init__(self):
        self.root = None
        self.selector = None
        self.directory = os.path.expanduser(r"C:\Users\thanh\Downloads\Programy\DigitalFusion\src")
        self.keyboard_controller = Controller()
        self.selector_open = False
        self.current_selection = 0
        print("Aplikace spuštěna. Čekám na '@' symbol...")

    def on_press(self, key):
        try:
            if key.char == '@':
                print("Detekován '@' symbol. Otevírám okno pro výběr souboru...")
                self.root.after(0, self.open_file_selector)
            elif key == Key.esc and self.selector_open:
                self.root.after(0, self.on_closing)
        except AttributeError:
            pass

    def open_file_selector(self):
        if self.selector_open:
            self.selector.lift()
            self.selector.focus_force()
            return

        self.selector = tk.Toplevel(self.root)
        self.selector.title("Select File")
        self.selector.attributes('-topmost', True)

        self.file_listbox = tk.Listbox(self.selector, height=15, width=50)
        self.file_listbox.pack(pady=10)

        self.search_entry = tk.Entry(self.selector, width=50)
        self.search_entry.pack(pady=5)
        self.search_entry.bind('<KeyRelease>', self.filter_files)

        self.load_files()

        self.selector.bind('<Return>', self.select_file)
        self.selector.bind('<Up>', self.move_selection)
        self.selector.bind('<Down>', self.move_selection)
        self.selector.bind('<Escape>', self.on_closing)
        self.selector.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.selector.after(100, self.focus_window)
        self.selector_open = True

    def focus_window(self):
        self.selector.focus_force()
        self.search_entry.focus_set()
        if os.name == 'nt':
            set_foreground_window(self.selector.winfo_id())

    def load_files(self):
        print(f"Načítám soubory z adresáře: {self.directory}")
        self.files = []
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, self.directory)
                self.files.append(rel_path)
        self.update_file_list()

    def update_file_list(self):
        self.file_listbox.delete(0, tk.END)
        for file in self.files:
            self.file_listbox.insert(tk.END, file)
        print(f"Zobrazeno {len(self.files)} souborů")
        self.current_selection = 0
        self.update_selection()

    def update_selection(self):
        if self.files:
            self.file_listbox.selection_clear(0, tk.END)
            self.file_listbox.selection_set(self.current_selection)
            self.file_listbox.see(self.current_selection)

    def filter_files(self, event):
        search_term = self.search_entry.get().lower()
        current_file = self.files[self.current_selection] if self.files else None
        self.files = []
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, self.directory)
                if search_term in rel_path.lower():
                    self.files.append(rel_path)
        self.update_file_list()
        if current_file in self.files:
            self.current_selection = self.files.index(current_file)
        self.update_selection()
        print(f"Filtrováno: {len(self.files)} souborů odpovídá vyhledávání '{search_term}'")

    def move_selection(self, event):
        if not self.files:
            return

        if event.keysym == 'Up':
            self.current_selection = max(0, self.current_selection - 1)
        elif event.keysym == 'Down':
            self.current_selection = min(len(self.files) - 1, self.current_selection + 1)

        self.update_selection()
        return 'break'

    def select_file(self, event):
        if self.files:
            selected_file = self.files[self.current_selection]
            file_path = os.path.join(self.directory, selected_file)
            print(f"Vybrán soubor: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            full_content = f"{file_path}\n\n{content}"
            pyperclip.copy(full_content)
            
            self.keyboard_controller.press(Key.backspace)
            self.keyboard_controller.release(Key.backspace)
            self.keyboard_controller.press(Key.ctrl)
            self.keyboard_controller.press('v')
            self.keyboard_controller.release('v')
            self.keyboard_controller.release(Key.ctrl)
            
            print(f"Obsah souboru vložen: {len(full_content)} znaků")
            self.on_closing(event)

    def on_closing(self, event=None):
        print("Zavírám okno pro výběr souboru")
        if self.selector:
            self.selector.destroy()
            self.selector = None
        self.selector_open = False

    def start_listening(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def run_tk(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.root.mainloop()

    def run(self):
        tk_thread = threading.Thread(target=self.run_tk)
        tk_thread.daemon = True
        tk_thread.start()
        self.start_listening()

if __name__ == "__main__":
    app = FileInsertApp()
    app.run()