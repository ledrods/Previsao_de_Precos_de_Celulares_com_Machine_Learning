import streamlit as st
import pandas as pd
from PIL import Image
import os

# Configuração inicial
st.set_page_config(page_title="Previsão de Preços de Celulares", layout="wide")

# --- 📊 ANÁLISE EXPLORATÓRIA ---
st.title("📊 Análise Exploratória de Dados")

df = pd.read_csv("data/celular2025_clean.csv") 
st.write("Aqui estão algumas estatísticas do conjunto de dados:")
st.dataframe(df.describe())

# Verificar coluna de marca
coluna_marca = None
possiveis_nomes = ["Company Name"]
for nome in possiveis_nomes:
    if nome in df.columns:
        coluna_marca = nome
        break

if coluna_marca is None:
    st.error("⚠️ Nenhuma coluna de marca encontrada. Verifique o dataset.")
else:
    # Calcular estatísticas básicas
    preco_medio = df["avg_price"].mean()
    preco_min = df["avg_price"].min()
    preco_max = df["avg_price"].max()
    marca_top = df.groupby(coluna_marca)["avg_price"].mean().idxmax()
    preco_marca_top = df.groupby(coluna_marca)["avg_price"].mean().max()

    # Exibir métricas principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="💰 Preço Médio dos celulares", value=f"US$ {preco_medio:,.2f}")
    col2.metric(label="📉 Celular Mais Barato", value=f"US$ {preco_min:,.2f}")
    col3.metric(label="📈 Celular Mais Caro", value=f"US$ {preco_max:,.2f}")
    col4.metric(label=f"🏆 Marca com a média mais alta ({marca_top})", value=f"US$ {preco_marca_top:,.2f}")

    st.markdown("---")

# --- 📊 MATRIZ DE CORRELAÇÃO ---
image1_path = "reports/matriz_correlacao_antiga.png"
image2_path = "reports/nova_matriz_correlacao.png"

if os.path.exists(image1_path) and os.path.exists(image2_path):
    with st.spinner("📷 Carregando imagens das matrizes de correlação..."):
        image1 = Image.open(image1_path).convert("RGB")
        image2 = Image.open(image2_path).convert("RGB")

        # Criar duas colunas para exibir as imagens lado a lado
        col1, col2 = st.columns(2)

        with col1:
            st.image(image1, caption="📌 Matriz de Correlação - Antes da Limpeza", use_container_width=True)

        with col2:
            st.image(image2, caption="✅ Matriz de Correlação - Após a Limpeza", use_container_width=True)

    # Explicação
    st.markdown("""
        ## 📌 Impacto da Limpeza de Dados na Matriz de Correlação

    A limpeza de dados foi fundamental para aprimorar a precisão da análise, especialmente na **matriz de correlação**.  
    Inicialmente, ao comparar o **preço dos celulares dos EUA** com a média do dataset, a correlação era de **0.28**, indicando uma relação fraca e distorcida.  
    Porém, após a **limpeza de dados**, essa correlação subiu para **0.99**, refletindo uma relação muito mais robusta e justa.

    ### 🔹 O Outlier e a Distorsão da Média
    Esse aumento na correlação se deve a um único **outlier** que estava **distorcendo a média** dos preços dos EUA.  
    Esse valor extremamente alto fazia com que a média fosse **inflacionada**, gerando uma comparação injusta com outros países.

    ### 🔍 Investigação do Outlier
    Busquei investigar a origem desse valor discrepante, considerando a possibilidade de que fosse um modelo de celular de **edição limitada**.  
    Contudo, percebi que se tratava de um **erro grosseiro no dataset**, onde um celular comum estava sendo listado a um preço exorbitante.

    ### 💱 Conversão de Moedas e Impacto na Análise
    Outro ponto crucial foi a **conversão dos preços para USD**, garantindo que a análise fosse consistente entre todas as moedas.  
    Cada preço foi **convertido com base nas taxas de câmbio do período**, permitindo comparações justas entre os valores de lançamento dos celulares em diferentes países.

    ✅ Após essa conversão, percebi que o **Paquistão teve a menor correlação com a média de preços, atingindo um coeficiente de 0.92**.  
    Isso sugere que os preços de lançamento no Paquistão apresentam **maior variação em relação ao valor médio global**.

    ### 🔥 Resultado da Limpeza de Dados
    A remoção do **outlier** e a **conversão das moedas** tiveram um **impacto direto na análise**, tornando a **média dos preços dos EUA mais representativa** e permitindo uma **comparação mais precisa** entre os preços dos celulares em diferentes países.
    """)

else:
    st.warning("⚠️ As imagens das matrizes de correlação não foram encontradas. Verifique os caminhos dos arquivos.")

st.markdown("""
## 🔍 Outliers nos Megapixels das Câmeras dos Celulares

Durante a análise, identifiquei **outliers nos megapixels das câmeras**, principalmente nos valores da câmera traseira.  
Havia modelos listados com **600 MP** e até **1000 MP**, o que não faz sentido no mercado atual.

### 🔹 Como Resolvi Esse Problema?
Para validar esses valores, utilizei **web scraping** em sites oficiais das fabricantes e lojas de tecnologia.  
Após essa etapa, descobri que:
- Algumas entradas estavam erradas devido a **dados inconsistentes na fonte original**.
- Alguns valores estavam representando **soma de múltiplas lentes**, e não o megapixel de uma única câmera.

✅ **Correção aplicada:** Removi outliers e considerei apenas valores reais encontrados no mercado.  
Após esse ajuste, a distribuição dos megapixels ficou muito mais coerente!
""")

# --- 📊 EVOLUÇÃO DOS PREÇOS ---
st.title("📊 Evolução dos Preços e Análise do Mercado de Smartphones")

image4_path = "reports/distribuicao_preco_medio.png"
image5_path = "reports/evolucao_samsung.png"
image6_path = "reports/histograma_preco_medio.png"


st.subheader("📌 Comparação Gráfica")


col1, col2 = st.columns(2)


if os.path.exists(image4_path):
    with col1:
        with st.spinner("📷 Carregando imagem de segmentação do mercado..."):
            st.image(Image.open(image4_path).convert("RGB"), caption="📌 Segmentação do Mercado de Smartphones", use_container_width=True)

if os.path.exists(image5_path):
    with col2:
        with st.spinner("📷 Carregando imagem da evolução dos preços da Samsung..."):
            st.image(Image.open(image5_path).convert("RGB"), caption="📈 Evolução dos Preços Médios da Samsung", use_container_width=True)

if os.path.exists(image6_path):
    with st.spinner("📷 Carregando imagem da distribuição dos preços médios..."):
        st.image(Image.open(image6_path).convert("RGB"), caption="📊 Distribuição dos Preços Médios dos Celulares", use_container_width=True)

# Explicação detalhada dos gráficos
st.markdown("""
            
### **📊 Gráfico 1: Segmentação do Mercado de Smartphones**
O **boxplot** do Gráfico 1 mostra uma clara divisão entre as marcas de smartphones com base no preço médio:

- **Marcas Acessíveis**: Nokia, Infinix e POCO, com preços médios mais baixos.
- **Marcas Intermediárias**: Xiaomi, Oppo e Motorola, com preços moderados.
- **Marcas Premium**: Apple, Samsung e Sony, com preços mais elevados.

Esse gráfico nos permite identificar a segmentação do mercado, que é crucial para entender as estratégias de marketing e posicionamento das marcas.

---

### **📈 Gráfico 2: Evolução dos Preços Médios da Samsung ao Longo dos Anos**
O **gráfico de linha** do Gráfico 2 revela a evolução dos preços médios da Samsung entre **2016 e 2024**.
Este gráfico ajuda a identificar as flutuações de preço da Samsung e como as suas estratégias de preços mudaram ao longo do tempo, com base nas inovações tecnológicas e mudanças nas preferências dos consumidores.

---

### **📊 Gráfico 3: Distribuição dos Preços Médios dos Celulares**
O **histograma** com curva de densidade do Gráfico 3 a **assimetria da distribuição**, com uma maior concentração de celulares acessíveis, mas uma minoria significativa de modelos premium, que afeta a média geral dos preços.

✅ **Conclusão**: A análise mostra que o **mercado de smartphones** é **diversificado**, com a maioria dos celulares posicionados na faixa de preços baixos, mas com **marcas premium** como **Samsung**, **Apple** e **Sony** se destacando em termos de preços mais altos. A **Samsung**, em particular, mostra uma tendência de **aumento de preços** ao longo dos anos (Gráfico 2), refletindo seu posicionamento como uma marca premium no mercado.

Esses insights são valiosos para entender as **estratégias de preços** das marcas e as **preferências dos consumidores** no competitivo mercado de smartphones. 🚀
""")
