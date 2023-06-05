import tkinter as tk
import ctypes
from recorder import ScreenRecorder

# Define o caminho para o arquivo de ícone
# Substitua "icone.ico" pelo nome do seu arquivo de ícone
icon_path = "assets/icone.ico"

# Define o ícone do aplicativo
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Screen Recorder")
ctypes.windll.kernel32.SetConsoleIcon(ctypes.windll.LoadLibraryW(icon_path))

# Iniciar o aplicativo
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Screen Recorder")
    root.geometry("400x200")

    ScreenRecorder(root)

    root.mainloop()
