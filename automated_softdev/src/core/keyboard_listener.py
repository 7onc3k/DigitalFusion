import keyboard
from utils.logger import get_logger
class KeyboardListener:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(__name__)
        self.callbacks = {}
    def add_hotkey(self, hotkey, callback):
        self.logger.info(f"Přidávám hotkey: {hotkey}")
        if hotkey == '@':
            keyboard.on_press(lambda e: callback() if e.name == '@' else None)
        else:
            keyboard.add_hotkey(hotkey, callback)
        self.callbacks[hotkey] = callback
    def remove_hotkey(self, hotkey):
        if hotkey in self.callbacks:
            self.logger.info(f"Odstraňuji hotkey: {hotkey}")
            keyboard.unhook_all_hotkeys()
            for k, v in self.callbacks.items():
                if k != hotkey:
                    self.add_hotkey(k, v)
            del self.callbacks[hotkey]
    def start_listening(self):
        self.logger.info("Začínám naslouchat klávesovým zkratkám")
    def stop_listening(self):
        self.logger.info("Končím naslouchání klávesovým zkratkám")
        keyboard.unhook_all()