import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import joblib
import matplotlib.pyplot as plt

def train_model():
    # Carregar os dados no padrão UTF-8
    data = pd.read_csv('data/responses_utf8.csv', encoding='utf-8')
    
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
    
    # Dividir os dados em treino e teste
    X = data[questions]
    y = data['curso_recomendado']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Treinar o modelo
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Avaliar o modelo
    y_pred = model.predict(X_test)
    print(f'Acurácia do modelo: {accuracy_score(y_test, y_pred):.2f}')
    print(classification_report(y_test, y_pred))
    
    # Visualizar a árvore de decisão
    plt.figure(figsize=(20, 10))
    plot_tree(model, feature_names=questions, class_names=model.classes_, filled=True, rounded=True)
    plt.title('Decision Tree')
    plt.show()  # Exibir a figura da árvore de decisão
    
    # Criar o diretório 'model' se não existir
    if not os.path.exists('model'):
        os.makedirs('model')
    
    # Salvar o modelo treinado
    joblib.dump(model, 'model/model.joblib')
    print("Modelo salvo com sucesso!")

if __name__ == "__main__":
    train_model()
