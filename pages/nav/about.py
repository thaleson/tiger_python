# pages/1_Sobre_o_Projeto.py
import streamlit as st

def about():
    st.title("📄 Sobre o Projeto")
    st.write("""
    ### Objetivo
    O objetivo deste projeto é ilustrar como os cassinos manipulam as probabilidades para garantir que, a longo prazo, a casa sempre vença.

    ### Funcionamento
    O **Jogo do Tigrinho** simula uma máquina caça-níquel com símbolos e probabilidades ajustadas para favorecer o "tigrinho". Embora o jogador possa ganhar algumas vezes, a manipulação garante que a casa tenha a vantagem.

    ### Tecnologias Utilizadas
    - **Python**: Linguagem de programação principal.
    - **Streamlit**: Biblioteca para criar a interface web interativa.
    """)

# Executar a função
about()
