import os
import time
from pynput import keyboard
from utils.logger import get_logger

if os.name == 'nt':
    import ctypes
    import win32gui
    import win32process

class WindowManager:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.keyboard_controller = keyboard.Controller()

    def get_foreground_window(self):
        if os.name == 'nt':
            return ctypes.windll.user32.GetForegroundWindow()
        else:
            self.logger.warning("Získání aktivního okna není podporováno na této platformě")
            return None

    def set_foreground_window(self, window_handle):
        if os.name == 'nt':
            ctypes.windll.user32.SetForegroundWindow(window_handle)
        else:
            self.logger.warning("Nastavení aktivního okna není podporováno na této platformě")

    def get_window_text(self, window_handle):
        if os.name == 'nt':
            length = ctypes.windll.user32.GetWindowTextLengthW(window_handle)
            buff = ctypes.create_unicode_buffer(length + 1)
            ctypes.windll.user32.GetWindowTextW(window_handle, buff, length + 1)
            return buff.value
        else:
            self.logger.warning("Získání textu okna není podporováno na této platformě")
            return ""

    def find_window_by_title(self, title):
        if os.name == 'nt':
            return ctypes.windll.user32.FindWindowW(None, title)
        else:
            self.logger.warning("Hledání okna podle titulku není podporováno na této platformě")
            return None

    def paste_content(self):
        time.sleep(0.1)  # Krátká pauza před vložením
        self.keyboard_controller.press(keyboard.Key.ctrl)
        self.keyboard_controller.press('v')
        time.sleep(0.1)
        self.keyboard_controller.release('v')
        self.keyboard_controller.release(keyboard.Key.ctrl)
        self.logger.info("Obsah vložen pomocí Ctrl+V")

    def get_process_name(self, window_handle):
        if os.name == 'nt':
            try:
                _, process_id = win32process.GetWindowThreadProcessId(window_handle)
                process_handle = win32process.OpenProcess(0x0400 | 0x0010, False, process_id)
                return win32process.GetModuleFileNameEx(process_handle, 0)
            except Exception as e:
                self.logger.error(f"Chyba při získávání názvu procesu: {str(e)}")
                return None
        else:
            self.logger.warning("Získání názvu procesu není podporováno na této platformě")
            return None