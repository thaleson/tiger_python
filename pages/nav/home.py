import streamlit as st

# Título e descrição da Home
def show_home():
    # Configurando o layout
    st.set_page_config(page_title="🐯 Projeto Jogo do Tigrinho 🐯", page_icon="🐯", layout="wide")

    # Título com um estilo atraente
    st.markdown(
        """
        <h1 style='text-align: center; color: #ff6347;'>🐯 Projeto Jogo do Tigrinho 🐯</h1>
        """,
        unsafe_allow_html=True
    )

    # Descrição com formatação
    st.markdown(
        """
        <div style='text-align: center; font-size: 18px; margin: 20px;'>
            Bem-vindo ao <strong>Projeto Jogo do Tigrinho</strong>! Este site demonstra como os cassinos e jogos de azar podem ser manipuláveis para favorecer a "casa". 
            <br><br>
            Navegue pelas opções na barra lateral para saber mais sobre o projeto ou para jogar o <strong>Jogo do Tigrinho</strong>.
        </div>
        """,
        unsafe_allow_html=True
    )
