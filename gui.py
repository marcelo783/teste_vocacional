import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Carregar o modelo treinado
model = joblib.load('model/model.joblib')

# Carregar o dataset de exemplo
questions = [
    "Você gosta de trabalhar com números? (1-5): ",
        "Você prefere trabalhar em equipe? (1-5): ",
        "Você tem interesse em tecnologia? (1-5): ",
        "Você gosta de resolver problemas complexos? (1-5): ",
        "Você prefere trabalhos criativos? (1-5): ",
        "Você gosta de aprender sobre biologia? (1-5): ",
        "Você gosta de escrever? (1-5): ",
        "Você prefere trabalhar ao ar livre? (1-5): ",
        "Você gosta de desenhar? (1-5): ",
        "Você prefere trabalhos práticos? (1-5): "
]

courses = ["Curso A", "Curso B", "Curso C", "Curso D", "Curso E", "Curso F", "Curso G", "Curso H", "Curso I", "Curso J"]

# Função para recomendar curso
def recommend_course():
    responses = []
    for entry in entries:
        try:
            value = int(entry.get())
            if value < 1 or value > 5:
                raise ValueError
            responses.append(value)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos (1-5) para todas as perguntas.")
            return
    
    # Fazer a previsão com o modelo
    prediction = model.predict([responses])[0]
    messagebox.showinfo("Recomendação de Curso", f"O curso recomendado para você é: {prediction}")

# Criar a janela principal
root = tk.Tk()
root.title("Teste Vocacional")

# Adicionar perguntas e campos de entrada
entries = []
for i, question in enumerate(questions):
    label = tk.Label(root, text=question)
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

# Adicionar botão para recomendar curso
recommend_button = tk.Button(root, text="Recomendar Curso", command=recommend_course)
recommend_button.pack()

# Iniciar o loop da interface gráfica
root.mainloop()
