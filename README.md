# 📱 Previsão de Preços de Celulares com Machine Learning

## 📚 Descrição

Este projeto visa aplicar técnicas de **aprendizado de máquina** para prever os preços de celulares com base em suas especificações técnicas. A previsão de preços ajuda a entender como características como **RAM**, **marca**, **capacidade de bateria**, **tamanho da tela**, entre outras, influenciam no valor de mercado de um celular.

O modelo utilizado para realizar a previsão foi o **XGBoost**, que demonstrou alto desempenho e precisão ao ser treinado com dados de preços históricos de celulares de diferentes marcas e especificações.

## 🔧 Tecnologias Utilizadas

- **Python**
- **Streamlit**: para construir o aplicativo interativo.
- **Pandas**: para manipulação de dados.
- **Plotly**: para criação de visualizações interativas.
- **XGBoost**: para modelagem preditiva.
- **Scikit-learn**: para pré-processamento e avaliação de modelos.
- **Matplotlib / Seaborn**: para visualizações estáticas.

## 📝 Objetivos

- Aplicar **modelos de aprendizado de máquina** para prever preços de celulares.
- Explorar a influência de diferentes características dos dispositivos móveis sobre o preço final.
- Criar um **aplicativo interativo** que permite que os usuários insiram características dos celulares e recebam previsões de preços.
- Aprofundar os conhecimentos na área de **análise de dados** e **modelagem preditiva**.

## 🔍 Como Funciona

1. **Previsão de Preço**: O modelo preditivo utiliza diversas características dos celulares, como **RAM**, **tamanho da tela**, **bateria**, **câmera** e **marca**, para prever o preço médio de mercado.
2. **Exploração dos Dados**: O aplicativo exibe gráficos interativos para análise exploratória dos dados, incluindo distribuições de preço por marca, segmentação de mercado e evolução de preços ao longo do tempo.
3. **Interface Interativa**: O Streamlit permite que os usuários explorem o projeto interativamente, visualizando os resultados e ajustando os parâmetros para obter previsões personalizadas.

## 🚀 Como Rodar o Projeto Localmente

### Requisitos

- **Python 3.8+**
- **Bibliotecas**: Você pode instalar as dependências do projeto usando o arquivo `requirements.txt`.

### Passos

1. Clone o repositório:

    ```bash
    git clone https://github.com/ledrods/previsao-precos-celulares.git
    ```

2. Navegue até a pasta do projeto:

    ```bash
    cd previsao-precos-celulares
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o aplicativo Streamlit:

    ```bash
    streamlit run app.py
    ```

5. Acesse o aplicativo no navegador através do endereço `http://localhost:8501`.

## 📊 Resultados e Análises

O projeto oferece diferentes visualizações e análises para explorar os dados de celulares, como:

- **Segmentação de mercado**: Gráficos de pizza segmentando os celulares em categorias como **Barato**, **Intermediário** e **Premium**.
- **Distribuição de Preços**: Histograma e boxplot para visualizar a distribuição de preços de acordo com as características dos celulares.
- **Evolução de Preços**: Gráfico de linha mostrando a evolução dos preços ao longo dos anos.
- **Top 10 Mais Caros e Mais Baratos**: Gráficos de barras mostrando os 10 celulares mais caros e mais baratos com base no preço médio.

## 📧 Contato

Para mais informações ou dúvidas, entre em contato comigo através das plataformas abaixo:

- **GitHub**: [https://github.com/ledrods](https://github.com/ledrods)
- **LinkedIn**: [https://www.linkedin.com/in/leandrodscesar/](https://www.linkedin.com/in/leandrodscesar/)
- **E-mail**: [leandro87dev@gmail.com](mailto:leandro87dev@gmail.com)

## 📄 Licença

Este projeto é de código aberto e pode ser utilizado e modificado livremente, desde que respeitada a **Licença MIT**.

---

**Leandro dos Santos Cesar**
