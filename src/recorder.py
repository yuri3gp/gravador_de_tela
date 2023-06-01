import tkinter as tk
from tkinter import filedialog
import threading
import cv2
import pyautogui
import numpy as np

class ScreenRecorder:
    def __init__(self, root):
        self.root = root
        
        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=20)
        
        self.stop_button = tk.Button(self.root, text="Stop Recording", state=tk.DISABLED, command=self.stop_recording)
        self.stop_button.pack(pady=10)
    
    def start_recording(self):
        self.root.iconify()  # Minimizar a janela principal
        
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        # Abrir diálogo de seleção de arquivo para salvar o vídeo
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4")
        if not file_path:
            self.reset_buttons()
            return
        
        # Obter as dimensões da tela
        screen_width, screen_height = pyautogui.size()
        
        # Configurar o gravador de vídeo
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(file_path, fourcc, 20.0, (screen_width, screen_height))
        
        self.is_recording = True
        
        # Thread para capturar e gravar os frames da tela
        def record_screen():
            while self.is_recording:
                # Capturar o frame atual da tela
                img = pyautogui.screenshot()
                
                # Converter a imagem capturada para um formato adequado para o OpenCV
                frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
                
                # Escrever o frame no arquivo de vídeo
                out.write(frame)
        
        self.recording_thread = threading.Thread(target=record_screen)
        self.recording_thread.start()
    
    def stop_recording(self):
        self.is_recording = False
        self.reset_buttons()
    
    def reset_buttons(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
