import streamlit as st
from datetime import date, timedelta

#Config da página
st.set_page_config("Tubetrend", layout="centered")

# Adicionar a imagem acima do título
st.image("app/images/logo.png", use_container_width=True)

# Titulo
st.title("Tubetrend")

#Subtitulo
st.subheader("Encontre vídeos virais no Youtube com base nos filtros personalizados.")

# CSS cor background
st.markdown("""
    <style>
    body {
        background-color: #4C8FC9FF;
        margin: 0;
        padding: 0;
    }
            .main {
        background-color: #4C8FC9FF;  /* Aplicando a cor de fundo também à área principal */
    }
    </style>
""", unsafe_allow_html=True)


#Filtros
st.markdown("### 🔍 Filtros de busca")

palavra_chave = st.text_input("Palavra chave", placeholder="Ex. biblia, histórias, fé...")

quantidade_filtros = st.slider("### Quantos vídeos deseja buscar?", min_value=1, max_value=50, value=10)

dias = st.slider("Buscar vídeos nos ultimos quantos dias?", min_value=1, max_value=10, value=7)

min_comentarios = st.number_input("Mínimo de comentários", min_value=0, max_value=100)

min_curtidas = st.number_input("Mínimo de curtidas", min_value=0, value=500)

min_inscritos = st.number_input("Mínimo de inscritos", min_value=0, max_value=1000)

st.selectbox("Permitir shorts", options=["Sim", "Não"])

if st.button("Buscar vídeos"):
    st.success("🔎 A busca será feita com os filtros selecionados (ainda sem conexão com YouTube)")


#Exibição dos vídeos
