import streamlit as st

st.title("🧠 Escolha do Modelo")

st.write("""
A escolha do modelo ideal para prever os preços dos celulares foi baseada em um processo rigoroso de testes e comparações entre diferentes algoritmos de aprendizado de máquina.  
Foram avaliados três modelos: **Random Forest, Gradient Boosting e XGBoost**, cada um conhecido por seu alto desempenho em problemas de regressão.

Para garantir a melhor precisão nas previsões, utilizamos métricas como **coeficiente de determinação (R²)** e **erro absoluto médio (MAE)**.  
O objetivo era encontrar um modelo que maximizasse a capacidade de explicação dos dados (R²) enquanto minimizava os erros nas previsões.
""")

st.subheader("📊 Comparação dos Modelos")

# Criando uma tabela com os resultados dos modelos
model_data = {
    "Modelo": ["Random Forest", "Gradient Boosting", "XGBoost"],
    "R² Médio": [0.8856, 0.8896, 0.8979],
    "MAE": [86.69, 105.04, 84.90]
}

st.table(model_data)

st.write("""
🔹 **Interpretação dos Resultados:**  
- O **Random Forest** apresentou um bom desempenho, mas teve um erro um pouco maior que o XGBoost.  
- O **Gradient Boosting**, apesar de um R² ligeiramente maior que o Random Forest, apresentou um MAE significativamente mais alto, o que indica previsões menos precisas.  
- O **XGBoost** superou os outros modelos, alcançando o maior R² (**0.8979**) e o menor MAE (**84.90**), tornando-se a melhor opção para prever os preços dos celulares.
""")

st.subheader("🚀 Por que escolhi o XGBoost?")

st.write("""
📌 **Melhor equilíbrio entre precisão e erro:** O XGBoost conseguiu reduzir os erros sem comprometer a capacidade de explicação do modelo.  
📌 **Alto desempenho em grandes volumes de dados:** Esse modelo é otimizado para eficiência computacional, lidando bem com conjuntos de dados maiores e complexos.  
📌 **Flexibilidade e capacidade de ajuste fino:** A possibilidade de ajustar hiperparâmetros no XGBoost ajudou a encontrar a melhor configuração para nosso problema.  

💡 **Com base nesses fatores, o XGBoost foi selecionado como o modelo ideal para prever o preço dos celulares, garantindo um alto nível de confiabilidade nas previsões.**
""")
