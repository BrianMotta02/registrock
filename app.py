import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from back import minimizar, tempo

def chamar_minimizar(janela):
    minimizar(janela)
    valor = e_intervalo.get()
    tempo(valor, janela)  # Agora passando a janela principal

def on_focus_in(event):
    if e_intervalo.get() == "Ex: 1h OU 15m":
        e_intervalo.delete(0, "end")
        e_intervalo.configure(foreground="white")

def on_focus_out(event):
    if e_intervalo.get() == "":
        e_intervalo.insert(0, "Ex: 1h OU 15m")
        e_intervalo.configure(foreground="gray")

co0 = "#000000"  # Preto absoluto

# Janela principal
janela = ttk.Window()
janela.geometry("530x770")
janela.configure(bg=co0)
janela.title("RegisTrock")

# Estilo
style = ttk.Style()
style.configure("preto.TFrame", background=co0)
style.configure("preto.TEntry", fieldbackground=co0, background=co0, foreground="gray")

# Carregando logo
image = Image.open("./logo.png")
logo = ImageTk.PhotoImage(image)

# Exibindo o logo
i_logo = ttk.Label(janela, image=logo)
i_logo.pack(pady=10)

# Frame principal
frame_corpo = ttk.Frame(janela, style="preto.TFrame")
frame_corpo.pack(fill="both", expand=True)

# Texto acima do Entry
l_texto = ttk.Label(frame_corpo, text="Digite o intervalo para o print:", font=("Arial", 12), background=co0, foreground="white")
l_texto.place(relx=0.5, rely=0.36, anchor="center")

# Campo Entry
e_intervalo = ttk.Entry(frame_corpo, style="preto.TEntry", font=("Arial", 11))
e_intervalo.place(relx=0.5, rely=0.42, anchor="center", width=250, height=40)

# Botão para iniciar
botao = ttk.Button(janela, text="Iniciar", bootstyle=("primary", "outline"), width=20, command=lambda: chamar_minimizar(janela))
botao.place(relx=0.5, rely=0.58, anchor="center", width=180, height=40)

# Configurações iniciais
e_intervalo.insert(0, "Ex: 1h OU 15m")
e_intervalo.bind("<FocusIn>", on_focus_in)
e_intervalo.bind("<FocusOut>", on_focus_out)

# Iniciar loop da janela
janela.mainloop()
