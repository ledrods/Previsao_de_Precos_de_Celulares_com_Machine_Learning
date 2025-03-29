import streamlit as st

st.title("📌 Sobre Mim")

st.write("""
Olá! Meu nome é **Leandro dos Santos Cesar**, sou estudante de **Sistemas de Informação** e sempre busquei oportunidades para aplicar na prática os conhecimentos adquiridos durante minha jornada acadêmica. Como parte dessa busca, decidi desenvolver este projeto de **previsão de preços de celulares** utilizando técnicas de **aprendizado de máquina**.

Este projeto surgiu da vontade de ganhar mais **experiência prática** na área de **análise de dados** e **modelagem preditiva**, explorando como **modelos de machine learning** podem ser aplicados para resolver problemas reais do dia a dia. A previsão do preço de um celular baseado em suas especificações técnicas, como **quantidade de RAM**, **marca**, **capacidade de bateria**, entre outras variáveis, foi o foco deste trabalho.

Para alcançar o melhor desempenho nas previsões, testei diferentes algoritmos de machine learning e optei pelo **XGBoost**, que se destacou por sua **precisão** e **eficiência**. O modelo final foi capaz de prever com alta exatidão os preços dos celulares, o que demonstra como podemos usar esses modelos para obter insights valiosos sobre o mercado de tecnologia.

Este projeto não só foi uma oportunidade de aprofundar meus conhecimentos, mas também de desenvolver habilidades que me tornarão mais preparado para atuar na área de **data science** e **machine learning**.

Fico feliz em compartilhar meu trabalho com você e, se quiser saber mais ou entrar em contato, pode me encontrar nas seguintes plataformas:
""")

# Links para o GitHub, LinkedIn e E-mail com ícones
st.markdown("""
<div style="display: flex; align-items: center; gap: 20px;">
    <a href="https://github.com/ledrods" target="_blank">
        <img src="https://img.shields.io/badge/-GitHub-000000?style=flat&logo=github" height="30px" use_container_width="true"/>
    </a>
    <a href="https://www.linkedin.com/in/leandrodscesar/" target="_blank">
        <img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=linkedin" height="30px" use_container_width="true"/>
    </a>
    <a href="mailto:leandro87dev@gmail.com" target="_blank">
        <img src="https://img.shields.io/badge/-E--mail-0077B5?style=flat&logo=gmail" height="30px" use_container_width="true"/>
    </a>
</div>
""", unsafe_allow_html=True)

# Sidebar de Navegação
st.sidebar.title("Navegação")
st.sidebar.markdown("Selecione uma página acima para explorar o projeto.")
