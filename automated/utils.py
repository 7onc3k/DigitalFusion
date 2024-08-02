import os
import ctypes
import time

def set_foreground_window(window_handle):
    if os.name == 'nt':
        ctypes.windll.user32.SetForegroundWindow(window_handle)

def get_foreground_window():
    if os.name == 'nt':
        return ctypes.windll.user32.GetForegroundWindow()
    return None

def get_window_text(hwnd):
    if os.name == 'nt':
        length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
        return buff.value
    return None

def find_window_by_title(title):
    if os.name == 'nt':
        return ctypes.windll.user32.FindWindowW(None, title)
    return None