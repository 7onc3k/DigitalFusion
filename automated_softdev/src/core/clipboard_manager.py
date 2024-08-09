import pyperclip
from utils.logger import get_logger
import threading
import time

class ClipboardManager:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(__name__)
        self.last_content = ''
        self.monitoring = False
        self.monitor_thread = None

    def get_content(self):
        return pyperclip.paste()

    def set_content(self, content):
        if self.config.append_to_clipboard:
            current_content = self.get_content()
            new_content = current_content + "\n\n" + content
            pyperclip.copy(new_content)
            self.logger.info("Obsah přidán do schránky")
        else:
            pyperclip.copy(content)
            self.logger.info("Obsah nahradil obsah schránky")
        
        self.last_content = content

    def start_monitoring(self, callback):
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_clipboard, args=(callback,))
        self.monitor_thread.start()

    def stop_monitoring(self):
        self.monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join()

    def _monitor_clipboard(self, callback):
        while self.monitoring:
            current_content = self.get_content()
            if current_content != self.last_content:
                self.logger.info("Detekována změna ve schránce")
                self.last_content = current_content
                callback(current_content)
            time.sleep(0.5)  # Kontrolujeme každých 500 ms