# pages/2_Jogo_do_Tigrinho.py
import streamlit as st
import random
from PIL import Image
from pathlib import Path
import time

def tiger_game():
    st.title("🎰 Jogo do Tigrinho 🎰")
    st.write("Bem-vindo ao **Jogo do Tigrinho**! Vamos testar sua sorte contra o tigrinho. 🐯")

    # Definindo os símbolos e probabilidades
    symbols = ['🍒', '🍋', '🍉', '⭐', '💎']
    symbols_images = {
        '🍒': 'cereja.png',
        '🍋': 'limao.png',
        '🍉': 'melancia.png',
        '⭐': 'estrela.png',
        '💎': 'diamante.png'
    }
    odds = [0.4, 0.3, 0.2, 0.07, 0.03]  # Probabilidades manipuladas

    # Função para girar o tigrinho
    def rotate_tigrinho():
        return random.choices(symbols, odds, k=3)

    # Função para calcular o prêmio
    def calculate_premium(roulette):
        if roulette[0] == roulette[1] == roulette[2]:
            if roulette[0] == '💎':
                return 100  # Maior prêmio para o símbolo 💎
            elif roulette[0] == '⭐':
                return 50   # Prêmio mediano para o símbolo ⭐
            else:
                return 10   # Prêmio pequeno para outros símbolos
        else:
            return 0  # Sem prêmio

    # Inicializar o estado do jogo
    if 'saldo' not in st.session_state:
        st.session_state.saldo = 100  # Saldo inicial
    if 'rodadas_restantes' not in st.session_state:
        st.session_state.rodadas_restantes = 10  # Número de rodadas
    if 'historico' not in st.session_state:
        st.session_state.historico = []

    # Função para jogar uma rodada
    def play():
        with st.spinner("🎰 Girando o Tigrinho..."):
            time.sleep(2)  # Simular um tempo de processamento
            if st.session_state.rodadas_restantes > 0 and st.session_state.saldo >= 10:
                st.session_state.saldo -= 10  # Custo por rodada
                resultado = rotate_tigrinho()
                premio = calculate_premium(resultado)
                st.session_state.saldo += premio
                if premio > 0:
                    st.session_state.rodadas_restantes += 1  # Ganha uma rodada adicional
                else:
                    st.session_state.rodadas_restantes -= 1  # Perde uma rodada
                st.session_state.historico.append({
                    'Rodada': len(st.session_state.historico) + 1,
                    'Resultado': resultado,
                    'Prêmio': premio,
                    'Rodadas Restantes': st.session_state.rodadas_restantes
                })
                st.session_state.ultimo_premio = premio
                st.session_state.ultimo_resultado = resultado
                if premio > 0:
                    st.success(f"🎉 Você ganhou {premio} pontos e uma rodada adicional!")
                else:
                    st.error("😞 Nada dessa vez! Você perdeu uma rodada.")
                st.balloons()  # Adicionando balões para efeito visual
            else:
                st.warning("⚠️ Você não tem mais rodadas ou saldo suficiente para jogar.")

    # Botão para girar o tigrinho com chave única
    if st.button("🎰 Girar o Tigrinho 🐯", key="play"):
        play()

    # Caminho para a pasta de imagens (relativo ao script atual)
    current_dir = Path(__file__).parent
    images_dir = current_dir.parent / 'images'

    # Exibir o resultado da última rodada com imagens
    if 'ultimo_resultado' in st.session_state:
        st.subheader("🎲 Resultado da Última Rodada:")
        col1, col2, col3 = st.columns(3)
        
        # Processar cada símbolo e exibir a imagem correspondente
        for idx, col in enumerate([col1, col2, col3]):
            simbolo = st.session_state.ultimo_resultado[idx]
            imagem_filename = symbols_images.get(simbolo, None)
            
            if imagem_filename:
                imagem_path = images_dir / imagem_filename
                if imagem_path.exists():
                    imagem = Image.open(imagem_path)
                    col.image(imagem, width=100)
                else:
                    col.error(f"🖼️ Imagem não encontrada: {imagem_filename}")
            else:
                col.error("❓ Símbolo desconhecido.")
        
        # Mensagem de prêmio
        if st.session_state.ultimo_premio > 0:
            st.success(f"🎉 Você ganhou {st.session_state.ultimo_premio} pontos!")
        else:
            st.error("😞 Nada dessa vez! Tente novamente.")

    # Exibir o saldo e rodadas restantes
    st.sidebar.header("📋 Status do Jogo")
    st.sidebar.write(f"**Saldo:** {st.session_state.saldo} pontos")
    st.sidebar.write(f"**Rodadas Restantes:** {st.session_state.rodadas_restantes}")

    # ============================================
    # NOVA SEÇÃO APRIMORADA: Histórico de Rodadas
    # ============================================
    st.subheader("📜 Histórico de Rodadas 📜")
    if st.session_state.historico:
        # Usando um container para o histórico
        historial_container = st.container()
        for rodada in reversed(st.session_state.historico):
            with historial_container:
                rodada_num = rodada['Rodada']
                resultado = rodada['Resultado']
                premio = rodada['Prêmio']
                rodadas_restantes = rodada['Rodadas Restantes']

                # Criar um card para cada rodada
                with st.container():
                    col1, col2 = st.columns([1, 3])
                    
                    # Coluna 1: Número da Rodada e Prêmio
                    with col1:
                        st.markdown(f"### Rodada {rodada_num}")
                        if premio > 0:
                            st.markdown(f"<div style='color:#FFA500; font-weight:bold;'>+{premio} pts 🎉</div>", unsafe_allow_html=True)
                        else:
                            st.markdown(f"<div style='color:#FF0000; font-weight:bold;'>-0 pts</div>", unsafe_allow_html=True)
                        st.markdown(f"**Rodadas Restantes:** {rodadas_restantes}")
                    
                    # Coluna 2: Imagens dos Símbolos
                    with col2:
                        cols = st.columns(3)
                        for idx, simbolo in enumerate(resultado):
                            imagem_filename = symbols_images.get(simbolo, None)
                            if imagem_filename:
                                imagem_path = images_dir / imagem_filename
                                if imagem_path.exists():
                                    imagem = Image.open(imagem_path)
                                    cols[idx].image(imagem, width=60)
                                else:
                                    cols[idx].error(f"🖼️ {imagem_filename} não encontrada")
                            else:
                                cols[idx].error("❓ Símbolo desconhecido")
                    
                    st.markdown("---")  # Linha separadora entre rodadas
    else:
        st.write("📭 Ainda não há rodadas jogadas.")

    # ============================================

    # Mensagem final quando o jogo termina
    if st.session_state.rodadas_restantes == 0:
        st.markdown("---")
        st.header("🏁 Jogo Encerrado 🏁")
        st.write(f"Seu saldo final foi de: **{st.session_state.saldo}** pontos.")
        st.error("😈 O tigrinho ganhou! Tente novamente para derrotá-lo.")
        st.write("### Obrigado por jogar!")
        # Botão de reiniciar com chave única
        if st.button("🔄 Reiniciar Jogo", key="reiniciar_jogo_rodadas"):
            st.session_state.saldo = 100
            st.session_state.rodadas_restantes = 10
            st.session_state.historico = []
            st.session_state.ultimo_premio = 0
            st.session_state.ultimo_resultado = []
    elif st.session_state.saldo < 10:
        st.markdown("---")
        st.header("🔚 Saldo Insuficiente")
        st.write(f"Seu saldo final foi de: **{st.session_state.saldo}** pontos.")
        st.error("😈 Você não tem saldo suficiente para continuar. O tigrinho ganhou!")
        st.write("### Obrigado por jogar!")
        # Botão de reiniciar com chave única
        if st.button("🔄 Reiniciar Jogo", key="reiniciar_jogo_saldo"):
            st.session_state.saldo = 100
            st.session_state.rodadas_restantes = 10
            st.session_state.historico = []
            st.session_state.ultimo_premio = 0
            st.session_state.ultimo_resultado = []

    # Explicação sobre a manipulação
    st.markdown("---")
    st.info("""
    **Nota:** Este jogo é manipulado para demonstrar como cassinos ajustam as probabilidades para favorecer a "casa". Embora você possa ganhar algumas rodadas, o design garante que, no longo prazo, o tigrinho (a casa) sempre vença.
    """)

# Executar a função
tiger_game()
