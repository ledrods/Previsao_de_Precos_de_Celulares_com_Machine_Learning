import pandas as pd
import streamlit as st
import joblib

# Carregar o modelo e o scaler salvos
modelo = joblib.load('C:/projeto1/analise_exploratoria/modelo/xgboost_model.pkl') 
scaler = joblib.load('C:/projeto1/analise_exploratoria/modelo/scaler.pkl') 

# Definir as colunas de entrada utilizadas no treinamento
X_columns = ['Mobile Weight', 'RAM', 'Front Camera', 'Back Camera', 
             'Battery Capacity', 'Screen Size', 'Launched Year'] 

# Função para prever o preço
def prever_preco(peso, ram, frente_camera, traseira_camera, bateria, tamanho_tela, ano_lancamento):
    entrada = pd.DataFrame({
        'Mobile Weight': [peso],
        'RAM': [ram],
        'Front Camera': [frente_camera],
        'Back Camera': [traseira_camera],
        'Battery Capacity': [bateria],
        'Screen Size': [tamanho_tela],
        'Launched Year': [ano_lancamento]
    })

    # Verificar se as colunas estão completas. Se alguma coluna estiver faltando, preencher com 0.
    cols_faltando = set(X_columns) - set(entrada.columns)
    for col in cols_faltando:
        entrada[col] = 0  

    entrada = entrada[X_columns]

    entrada_scaled = scaler.transform(entrada)

    preco_estimado = modelo.predict(entrada_scaled)[0]

    return preco_estimado

# Interface com o Streamlit
st.title("💡 Prevendo o Preço do Celular")

# Inputs do usuário
peso = st.slider("Peso do celular (gramas)", min_value=100, max_value=900, step=10, value=160)
ram = st.selectbox("Quantidade de RAM (GB)", [2, 4, 6, 8, 12, 16], key="ram")
frente_camera = st.slider("Megapixels da câmera frontal", min_value=1, max_value=200, step=1, value=12)
traseira_camera = st.slider("Megapixels da câmera traseira", min_value=1, max_value=200, step=1, value=48)
bateria = st.slider("Capacidade da bateria (mAh)", min_value=1000, max_value=12000, step=100, value=3500)
tamanho_tela = st.slider("Tamanho da tela (polegadas)", min_value=4.0, max_value=9.0, step=0.1, value=6.0)
ano_lancamento = st.selectbox("Ano de lançamento", [2020, 2021, 2022, 2023, 2024, 2025], key="ano_lancamento")

# Prever o preço
if st.button("Prever Preço"):
    preco_estimado = prever_preco(peso, ram, frente_camera, traseira_camera, bateria, tamanho_tela, ano_lancamento)
    if preco_estimado is not None:
        st.write(f"Preço estimado: ${preco_estimado:,.2f}")
