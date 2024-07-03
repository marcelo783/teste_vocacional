

import joblib
import pandas as pd
from questionnaire import get_questionnaire

def recommend_course():
    # Carregar o modelo treinado
    model = joblib.load('model/model.joblib')
    
    # Coletar novas respostas do questionário
    questions = get_questionnaire()
    responses = []
    
    print("Responda ao questionário abaixo:")
    for question in questions:
        response = input(f"{question} (1-5): ")
        responses.append(response)
    
    # Fazer a previsão
    new_data = pd.DataFrame([responses], columns=questions)
    predicted_course = model.predict(new_data)
    print(f'Curso recomendado: {predicted_course[0]}')

if __name__ == "__main__":
    recommend_course()
