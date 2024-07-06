

import csv

def collect_data():
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

    responses = []
    for question in questions:
        while True:
            try:
                response = int(input(question))
                if 1 <= response <= 5:
                    responses.append(response)
                    break
                else:
                    print("Por favor, insira um número entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 5.")

    recommended_course = input("Qual curso você recomendaria? (Ex: Curso A, Curso B, Curso C, ...) ")

    with open('data/responses_utf8.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(responses + [recommended_course])
    print("Respostas salvas com sucesso!")

if __name__ == "__main__":
    collect_data()
