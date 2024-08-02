import tkinter as tk
import os
from pynput import keyboard
from pynput.keyboard import Key, Controller
import threading
import pyperclip
import time
from file_selector import FileSelector
from utils import set_foreground_window, get_foreground_window, get_window_text, find_window_by_title

class FileInsertApp:
    def __init__(self):
        self.root = None
        self.selector = None
        self.directory = os.path.abspath(r"C:\Users\thanh\Downloads\Programy\DigitalFusion\src")
        self.keyboard_controller = Controller()
        self.selector_open = False
        self.target_window = None
        print("Aplikace spuštěna. Čekám na '@' symbol...")

    def on_press(self, key):
        try:
            if key.char == '@':
                print("Detekován '@' symbol. Otevírám okno pro výběr souboru...")
                self.target_window = get_foreground_window()
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

        self.selector = FileSelector(self.root, self.directory, self.on_files_selected, self.on_closing)
        self.selector_open = True

    def on_files_selected(self, file_paths):
        print(f"Vybráno souborů: {len(file_paths)}")
        content = ""
        for file_path in file_paths:
            content += f"--- File: {file_path} ---\n"
            with open(file_path, 'r', encoding='utf-8') as file:
                content += file.read()
            content += "\n\n"
        
        pyperclip.copy(content)
        print(f"Obsah zkopírován do clipboardu: {len(content)} znaků")

        set_foreground_window(self.target_window)
        time.sleep(0.1)

        self.keyboard_controller.press(Key.ctrl)
        self.keyboard_controller.press('v')
        time.sleep(0.1)
        self.keyboard_controller.release('v')
        self.keyboard_controller.release(Key.ctrl)
        
        clipboard_content = pyperclip.paste()
        print(f"Obsah clipboardu po vložení: {len(clipboard_content)} znaků")
        
        print(f"Obsah souborů vložen: {len(content)} znaků")
        self.on_closing()

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