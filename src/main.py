import tkinter as tk
from recorder import ScreenRecorder

# Iniciar o aplicativo
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Screen Recorder")
    root.geometry("400x200")
    
    ScreenRecorder(root)
    
    root.mainloop()
