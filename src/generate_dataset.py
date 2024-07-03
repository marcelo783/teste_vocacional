
import pandas as pd

data = {
    "Você gosta de trabalhar com números?": [5, 2, 4, 1, 3, 5, 2, 4, 1, 3],
    "Você prefere trabalhar em equipe?": [4, 5, 2, 3, 4, 5, 2, 3, 4, 5],
    "Você tem interesse em tecnologia?": [5, 1, 4, 3, 2, 5, 1, 4, 3, 2],
    "Você gosta de resolver problemas complexos?": [5, 4, 1, 3, 2, 5, 4, 1, 3, 2],
    "Você prefere trabalhos criativos?": [3, 5, 4, 1, 2, 3, 5, 4, 1, 2],
    "Você gosta de aprender sobre biologia?": [1, 5, 2, 4, 3, 1, 5, 2, 4, 3],
    "Você gosta de escrever?": [5, 2, 4, 1, 3, 5, 2, 4, 1, 3],
    "Você prefere trabalhar ao ar livre?": [2, 5, 3, 4, 1, 2, 5, 3, 4, 1],
    "Você gosta de desenhar?": [4, 5, 1, 3, 2, 4, 5, 1, 3, 2],
    "Você prefere trabalhos práticos?": [5, 2, 4, 1, 3, 5, 2, 4, 1, 3],
    "curso_recomendado": [
        "Engenharia", 
        "Psicologia", 
        "Ciência da Computação", 
        "Design Gráfico", 
        "Biologia", 
        "Jornalismo", 
        "Agronomia", 
        "Arquitetura", 
        "Administração", 
        "Direito"
    ]
}

df = pd.DataFrame(data)
df.to_csv('data/responses_utf8.csv', index=False, encoding='utf-8')

print("Dataset gerado com sucesso!")
