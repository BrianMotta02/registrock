import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from PIL import Image, ImageTk
from datetime import datetime

screenshot_dir = "./"
lista_descricao = []


arquivo_path = os.path.join(os.getcwd(), 'descricao.txt')


if os.path.exists(arquivo_path):
    with open(arquivo_path, 'r') as arquivo:
        lista_descricao = arquivo.readlines()


screenshots_janela = ttk.Window()
screenshots_janela.geometry("700x900")
screenshots_janela.configure(bg="#000000")
screenshots_janela.title("Todos os Screenshots")


style = ttk.Style()
style.configure("preto.TFrame", background="#000000")
style.configure("preto.TLabel", background="#000000", foreground="white")
style.configure("preto.TEntry", fieldbackground="#000000", background="#000000", foreground="gray")


canvas = ttk.Canvas(screenshots_janela, bg="#000000", highlightthickness=0)
scrollbar = ttk.Scrollbar(screenshots_janela, orient=VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)


frame_corpo = ttk.Frame(canvas, style="preto.TFrame")
canvas.create_window((0, 0), window=frame_corpo, anchor="nw")


scrollbar.pack(side=RIGHT, fill=Y)
canvas.pack(side=LEFT, fill=BOTH, expand=True)


existing_screenshots = [
    f for f in os.listdir(screenshot_dir) if f.startswith("screenshot_") and f.endswith(".png")
]


screenshots = sorted(existing_screenshots, key=lambda x: os.path.getmtime(os.path.join(screenshot_dir, x)), reverse=False)


y_position = 0.05
for index, screenshot in enumerate(screenshots):

    screenshot_path = os.path.join(screenshot_dir, screenshot)
    image = Image.open(screenshot_path)
    image = image.resize((460, 300), Image.Resampling.LANCZOS)
    screen = ImageTk.PhotoImage(image)


    i_screen = ttk.Label(frame_corpo, image=screen, style="preto.TLabel")
    i_screen.image = screen
    i_screen.grid(row=index*3, column=0, padx=100, pady=10, columnspan=2)


    timestamp = os.path.getmtime(screenshot_path)
    date_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    l_data = ttk.Label(frame_corpo, text=f"Data: {date_time}", font=("Arial", 10), style="preto.TLabel")
    l_data.grid(row=index*3 + 1, column=0, padx=100, pady=5, columnspan=2)


    descricao = lista_descricao[index].strip() if index < len(lista_descricao) else "Sem descrição"
    l_descricao = ttk.Label(frame_corpo, text=f"Descrição: {descricao}", font=("Arial", 10), style="preto.TLabel")
    l_descricao.grid(row=index*3 + 2, column=0, padx=100, pady=5, columnspan=2)


    y_position += 0.3


frame_corpo.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))


screenshots_janela.configure(bg="#000000")
canvas.configure(bg="#000000")

# Iniciar loop da janela
screenshots_janela.mainloop()
