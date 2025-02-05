import tkinter as tk
import subprocess
import pyautogui
import time
import os

lista_descricao = {}

screenshot_dir = "./"


def minimizar(janela):
    janela.iconify()

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

    # Usando after() para garantir que a interface seja chamada na thread principal
    root.after(tempo_segundos * 1000, exibe_tela)

def exibe_tela():
    # Listar arquivos que começam com "screenshot_" e terminam com ".png"
    existing_screenshots = [
        f for f in os.listdir(screenshot_dir) if f.startswith("screenshot_") and f.endswith(".png")
    ]
    
    # Contar quantos existem e definir o próximo número
    next_number = len(existing_screenshots) + 1
    screenshot_path = os.path.join(screenshot_dir, f'screenshot_{next_number}.png')

    # Tirar print e salvar com o próximo número
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)  

    # Chamar o script da interface gráfica
    subprocess.run(["python", "descrever.py"])

def salvar(descricao):
    lista_descricao.append(descricao)