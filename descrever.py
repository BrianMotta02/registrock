import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from PIL import Image, ImageTk
from back import salvar


def chamar_salvar():
    descricao = campo_texto.get()
    descricao_janela.destroy()
    salvar(descricao)

screenshot_dir = "./"

existing_screenshots = [
        f for f in os.listdir(screenshot_dir) if f.startswith("screenshot_") and f.endswith(".png")
    ]
    
next_number = len(existing_screenshots)
screenshot_path = os.path.join(screenshot_dir, f'screenshot_{next_number}.png')

# Criando a janela de descrição
descricao_janela = ttk.Window()
descricao_janela.geometry("700x700")
descricao_janela.configure(bg="#000000")
descricao_janela.title("RegisTrock")

# Criando o estilo ANTES dos widgets
style = ttk.Style()
style.configure("preto.TFrame", background="#000000")
style.configure("preto.TEntry", fieldbackground="#000000", background="#000000", foreground="gray")

# Frame principal
frame_corpo = ttk.Frame(descricao_janela, style="preto.TFrame")
frame_corpo.pack(fill="both", expand=True)

image = Image.open(screenshot_path)
image = image.resize((460, 300), Image.Resampling.LANCZOS)

screen = ImageTk.PhotoImage(image)

# Exibindo o logo
i_screen = ttk.Label(descricao_janela, image=screen)
i_screen.place(relx=0.5, rely=0.27, anchor="center")

# Texto para descrição
l_texto = ttk.Label(frame_corpo, text="Descreva o que estava fazendo:", font=("Arial", 12), background="#000000", foreground="white")
l_texto.place(relx=0.5, rely=0.55, anchor="center")

# Campo de texto para descrição
campo_texto = ttk.Entry(frame_corpo, font=("Arial", 12))
campo_texto.place(relx=0.5, rely=0.65, anchor="center", width=300)

# Botão de envio
botao_enviar = ttk.Button(frame_corpo, text="Enviar", bootstyle=("primary", "outline"), width=20, command=chamar_salvar)
botao_enviar.place(relx=0.5, rely=0.76, anchor="center")
# Iniciar loop da janela
descricao_janela.mainloop()