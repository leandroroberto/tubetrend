import streamlit as st
from datetime import date, timedelta
from youtube_api import buscar_videos


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

st.text_input("Palavra chave", placeholder="Ex. biblia, histórias, fé...")

st.slider("### Quantos vídeos deseja buscar?", min_value=1, max_value=50, value=10)

st.slider("Buscar vídeos nos ultimos quantos dias?", min_value=1, max_value=10, value=7)

st.number_input("Mínimo de comentários", min_value=0, max_value=100)

st.number_input("Mínimo de curtidas", min_value=0, value=500)

st.number_input("Mínimo de inscritos", min_value=0, max_value=1000)

st.selectbox("Permitir shorts", options=["Sim", "Não"])


#CSS
st.markdown("""
    <style>
        .video-container{
            height: 350px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .video-title{
            font-size: 14px;
            font-weight: bold;
            text-align: center;
        }

        .video-channel{
            font-size: 12px;
            text-align: center;
        }
    </style>

""", unsafe_allow_html=True)


# Buscar vídeos

col1, col2 = st.columns(2)
colunas = [col1, col2]

if st.button("Buscar vídeos"):
    resultados = buscar_videos(palavra_chave=titulo_busca, max_results={quantidade_videos})

    for i,  item in enumerate(resultados["items"]):
        video_id = item["id"]["videoId"]
        titulo = item["snippet"]["title"]
        canal = item["snippet"]["channelTitle"]
        thumbnail = item["snippet"]["thumbnails"]["high"]["url"]
        
        with colunas[i % 2]:
            st.markdown('<div class="video-container">', unsafe_allow_html=True)
            st.image(thumbnail, use_container_width=False, width=300)
            st.markdown(f'<div class="video-title">{titulo}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="video-channel">{canal}</div>', unsafe_allow_html=True)
            st.markdown(f"[Assistir no Youtube](https://www.youtube.com/watch?v={video_id})")
            st.markdown('</div>', unsafe_allow_html=True)