# app.py
import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(
    page_title="Projeto Jogo do Tigrinho",
    page_icon="🐯",
    layout="centered",
    initial_sidebar_state="auto",
)
# Aplicar estilos de CSS à página (se houver)
try:
    with open("static/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Arquivo de estilo CSS não encontrado!")


# Menu de Navegação Personalizado na Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Navegação",
        options=["Home", "Sobre o Projeto", "Jogo do Tigrinho"],
        icons=["house", "info-circle", "coin"],
        menu_icon="cast",
        default_index=0,
    )



# Importar páginas de navegação

if selected == "Home":
    from pages.nav.home import show_home
    show_home()
elif selected == "Sobre o Projeto":
    from pages.nav.about import about
    about()
elif selected == "Jogo do Tigrinho":
    from pages.nav.play_game import tiger_game
    tiger_game()
