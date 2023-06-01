import cv2
import pyautogui
import numpy as np
import keyboard

# Definir o nome do arquivo de saída
output_file = 'screen_capture.mp4'

# Obter as dimensões da tela
screen_width, screen_height = pyautogui.size()

# Configurar o gravador de vídeo
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, 20.0, (screen_width, screen_height))

# Variável para controlar a pausa
paused = False

# Loop para capturar e gravar os frames da tela
while True:
    # Verificar se a tecla 'p' foi pressionada para pausar a gravação
    if keyboard.is_pressed('p'):
        paused = not paused

    if not paused:
        # Capturar o frame atual da tela
        img = pyautogui.screenshot()

        # Converter a imagem capturada para um formato adequado para o OpenCV
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Escrever o frame no arquivo de vídeo
        out.write(frame)

    # Verificar se a tecla 'q' foi pressionada para parar a gravação
    if keyboard.is_pressed('q'):
        break

# Liberar recursos
out.release()
cv2.destroyAllWindows()
