# PapiWeb desarrollos informaticos
# PapiDech CDA-117 es un proyecto de interfaz digital de audio y video inspirado en el estilo retro-futurista de los años 80. Utiliza Streamlit para crear una experiencia visual única, combinando videos con marcos gráficos personalizados. El proyecto permite a los usuarios cargar su propia música en formato MP3 para acompañar la reproducción de videos, creando una experiencia multimedia interactiva. Con un diseño neón y una estética cyberpunk, PapiDech CDA-117 ofrece una plataforma para disfrutar de contenido audiovisual de manera innovadora y estilizada.
import streamlit as st
import base64
import os
import random

# =========================
# CONFIGURACIÓN Y ESTILOS
# =========================
st.set_page_config(page_title="PapiDech CDA-117", layout="wide")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Estilo Neón y Posicionamiento
st.markdown("""
<style>
    .stApp { background-color: #050505; }
    .player-box {
        position: relative;
        width: 1000px;
        margin: auto;
    }
    .vid-layer {
        position: absolute;
        top: 75px; 
        left: 337px;
        width: 566px;
        height: 225px;
        z-index: 1;
        object-fit: cover;
    }
    .marco-layer {
        position: relative;
        width: 1000px;
        z-index: 2;
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# LÓGICA DE ESTADO
# =========================
if 'current_vid' not in st.session_state:
    st.session_state.current_vid = random.randint(1, 5)

# =========================
# PROCESAMIENTO BASE64
# =========================
# Cargamos solo lo necesario para esta ejecución
try:
    marco_uri = f"data:image/png;base64,{get_base64('static/marco_papiweb.png')}"
    video_uri = f"data:video/mp4;base64,{get_base64(f'static/sample{st.session_state.current_vid}.mp4')}"
except FileNotFoundError as e:
    st.error(f"Falta un archivo esencial: {e}")
    st.stop()

# =========================
# RENDERIZADO
# =========================
st.markdown(f"""
<div class="player-box">
    <video class="vid-layer" autoplay loop muted playsinline>
        <source src="{video_uri}" type="video/mp4">
    </video>
    <img src="{marco_uri}" class="marco-layer">
</div>
""", unsafe_allow_html=True)

# Controles inferiores
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⏭ SIGUIENTE SHOW (Random)"):
        st.session_state.current_vid = random.randint(1, 5)
        st.rerun()

with col2:
    audio_file = st.file_uploader("🎵 CARGAR MP3", type=["mp3"])
    if audio_file:
        st.audio(audio_file, autoplay=True)

st.caption("PAPIWEB DIGITAL AUDIO & VIDEO INTERFACE - CDA-117 ONLINE")
