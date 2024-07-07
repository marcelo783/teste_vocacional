import os
import joblib
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

def visualize_tree():
    # Carregar o modelo treinado
    model_path = 'model/model.joblib'
    if not os.path.exists(model_path):
        print(f"Modelo não encontrado em {model_path}. Treine o modelo primeiro.")
        return
    
    model = joblib.load(model_path)
    
    # Definir os nomes das colunas
    questions = [
        "Você gosta de trabalhar com números?",
        "Você prefere trabalhar em equipe?",
        "Você tem interesse em tecnologia?",
        "Você gosta de resolver problemas complexos?",
        "Você prefere trabalhos criativos?",
        "Você gosta de aprender sobre biologia?",
        "Você gosta de escrever?",
        "Você prefere trabalhar ao ar livre?",
        "Você gosta de desenhar?",
        "Você prefere trabalhos práticos?"
    ]
    
    # Visualizar a árvore de decisão
    plt.figure(figsize=(20, 10))
    plot_tree(model, feature_names=questions, class_names=model.classes_, filled=True, rounded=True)
    plt.title('Decision Tree')
    plt.show()

if __name__ == "__main__":
    visualize_tree()
