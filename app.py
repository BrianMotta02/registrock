import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from back import tempo, salvar, visualizar
import os

diretorio = "./"

for arquivo in os.listdir(diretorio):
    if arquivo.startswith("screenshot") or arquivo.startswith("descricao"):
        arquivo_path = os.path.join(diretorio, arquivo)
        os.remove(arquivo_path)


def chamar_minimizar():
    janela.iconify()
    valor = e_intervalo.get()
    tempo(valor, janela)


def on_focus_in(event):
    if e_intervalo.get() == "Ex: 1h OU 15m":
        e_intervalo.delete(0, "end")
        e_intervalo.configure(foreground="white")

def on_focus_out(event):
    if e_intervalo.get() == "":
        e_intervalo.insert(0, "Ex: 1h OU 15m")
        e_intervalo.configure(foreground="gray")


def visualizar_log():
    visualizar()


co0 = "#000000"


janela = ttk.Window()
janela.geometry("530x770")
janela.configure(bg=co0)
janela.title("RegisTrock - Brian Motta")
janela.iconbitmap("./RT.ico")


style = ttk.Style()
style.configure("preto.TFrame", background=co0)
style.configure("preto.TEntry", fieldbackground=co0, background=co0, foreground="gray")


image = Image.open("./logo.png")
logo = ImageTk.PhotoImage(image)


i_logo = ttk.Label(janela, image=logo)
i_logo.pack(pady=10)


frame_corpo = ttk.Frame(janela, style="preto.TFrame")
frame_corpo.pack(fill="both", expand=True)


l_texto = ttk.Label(frame_corpo, text="Digite o intervalo para o print:", font=("Arial", 12), background=co0, foreground="white")
l_texto.place(relx=0.5, rely=0.36, anchor="center")


e_intervalo = ttk.Entry(frame_corpo, style="preto.TEntry", font=("Arial", 11))
e_intervalo.place(relx=0.5, rely=0.42, anchor="center", width=250, height=40)


botao_iniciar = ttk.Button(janela, text="Iniciar", bootstyle=("primary", "outline"), width=20, command=chamar_minimizar)
botao_iniciar.place(relx=0.37, rely=0.58, anchor="center", width=125, height=40)


botao_visualizar = ttk.Button(janela, text="Visualizar", bootstyle=("primary", "outline"), width=20, command=visualizar_log)
botao_visualizar.place(relx=0.63, rely=0.58, anchor="center", width=125, height=40)


e_intervalo.insert(0, "Ex: 1h OU 15m")
e_intervalo.bind("<FocusIn>", on_focus_in)
e_intervalo.bind("<FocusOut>", on_focus_out)


janela.mainloop()