import tkinter as tk
import subprocess
import pyautogui
import time
import os

screenshot_dir = "./"

def tempo(valor, root):
    try:
        if 'h' in valor:
            tempo_segundos = int(valor.replace('h', '')) * 3600  
        elif 'm' in valor:
            tempo_segundos = int(valor.replace('m', '')) * 60  
        else:
            tempo_segundos = int(valor)
    except ValueError:
        print("Erro: o formato do valor fornecido não é válido.")
        return


    root.after(tempo_segundos * 1000, exibe_tela)
    root.after(tempo_segundos * 1000, lambda: tempo(valor, root))

def exibe_tela():

    existing_screenshots = [
        f for f in os.listdir(screenshot_dir) if f.startswith("screenshot_") and f.endswith(".png")
    ]
    

    next_number = len(existing_screenshots) + 1
    screenshot_path = os.path.join(screenshot_dir, f'screenshot_{next_number}.png')


    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)  


    subprocess.run(["python", "descrever.py"])

def salvar(descricao):

    arquivo_path = os.path.join(os.getcwd(), 'descricao.txt')
    

    with open(arquivo_path, 'a') as arquivo:

        arquivo.write(descricao + '\n')

def visualizar():
    subprocess.run(["python", "visualizar_log.py"])