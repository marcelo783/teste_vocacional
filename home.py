import tkinter as tk
import subprocess
import sys  # Importar sys para obter o caminho do Python atual

def open_questionnaire():
    root.destroy()  # Fechar a janela atual
    subprocess.Popen([sys.executable, 'gui.py'])  # Usar sys.executable para obter o Python atual

def show_questionnaire():
    root = tk.Tk()
    root.title("Questionário")
    
    # Definir as perguntas e descrição da escala
    description = (
        "Por favor, responda às perguntas a seguir usando a seguinte escala:\n"
        "1 = Nunca\n"
        "2 = Raramente\n"
        "3 = Às vezes\n"
        "4 = Frequentemente\n"
        "5 = Sempre"
    )
    
    label_title = tk.Label(root, text="Teste Vocacional", font=("Arial", 18))
    label_title.pack(pady=10)
    
    label_description = tk.Label(root, text=description, justify="left")
    label_description.pack(pady=20)
    
    button_start = tk.Button(root, text="Iniciar Questionário", command=open_questionnaire)
    button_start.pack()
    
    root.mainloop()

# Criar a janela principal
root = tk.Tk()
root.title("Teste Vocacional")

# Definir título e descrição inicial
label_title = tk.Label(root, text="Teste Vocacional", font=("Arial", 18))
label_title.pack(pady=10)

label_description = tk.Label(root, text="Bem-vindo ao teste vocacional! Este teste ajudará a recomendar cursos com base em suas preferências.", justify="left")
label_description.pack(pady=20)

button_next = tk.Button(root, text="Ir para o Questionário", command=show_questionnaire)
button_next.pack()

root.mainloop()
