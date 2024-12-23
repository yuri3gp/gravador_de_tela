import os
import sys
import tkinter as tk
import ctypes
from recorder import ScreenRecorder
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "assets", "icon.ico")

if not os.path.exists(icon_path):
    raise FileNotFoundError(f"Ícone não encontrado: {icon_path}")
ctypes.windll.kernel32.SetConsoleIcon(ctypes.windll.kernel32.LoadLibraryW(icon_path))
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Screen Recorder")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Screen Recorder")
    root.geometry("400x200")

    ScreenRecorder(root)

    root.mainloop()
