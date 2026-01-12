# Papiweb desarrollos informaticos
import streamlit as st
import base64
import os
import random

# =========================
# CONFIGURACIÓN Y ESTILOS
# =========================
st.set_page_config(page_title="PapiDech CDA-117", layout="wide")

def get_base64(bin_file):
    # Asegúrate de que el archivo exista para evitar crash
    if not os.path.exists(bin_file):
        return None 
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
marco_b64 = get_base64('static/marco_papiweb.png')
video_b64 = get_base64(f'static/sample{st.session_state.current_vid}.mp4')

if not marco_b64 or not video_b64:
    st.error("Error: No se encuentran los archivos en la carpeta 'static/'. Verifica nombres y rutas.")
    st.stop()

marco_uri = f"data:image/png;base64,{marco_b64}"
video_uri = f"data:video/mp4;base64,{video_b64}"

# =========================
# RENDERIZADO
# =========================
# Nota: Usamos una key única en el HTML o cambiamos el contenido para forzar al navegador a repintar
html_code = f"""
<div class="player-box">
    <video class="vid-layer" autoplay loop muted playsinline>
        <source src="{video_uri}" type="video/mp4">
    </video>
    <img src="{marco_uri}" class="marco-layer">
</div>
"""
st.markdown(html_code, unsafe_allow_html=True)

# Controles inferiores
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⏭ SIGUIENTE SHOW (Random)"):
        # Lógica para evitar repetir el mismo video
        current = st.session_state.current_vid
        new_vid = random.randint(1, 5)
        while new_vid == current:
            new_vid = random.randint(1, 5)
            
        st.session_state.current_vid = new_vid
        st.rerun()

with col2:
    audio_file = st.file_uploader("🎵 CARGAR MP3", type=["mp3"])
    if audio_file:
        st.audio(audio_file, autoplay=True)

st.caption("PAPIWEB DIGITAL AUDIO & VIDEO INTERFACE - CDA-117 ONLINE")