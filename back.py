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

    # Chama a função de exibição da tela e inicia novamente após o tempo estipulado
    root.after(tempo_segundos * 1000, exibe_tela)  # Exibe a tela após o tempo
    root.after(tempo_segundos * 1000, lambda: tempo(valor, root))  # Reaplica o ciclo após o mesmo intervalo

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
    # Definindo o caminho do arquivo
    arquivo_path = os.path.join(os.getcwd(), 'descricao.txt')
    
    # Abrir o arquivo em modo de adição ('a')
    with open(arquivo_path, 'a') as arquivo:
        # Escrever a descrição no arquivo
        arquivo.write(descricao + '\n')  # Adiciona uma nova linha após cada descrição

def visualizar():
    subprocess.run(["python", "visualizar_log.py"])
