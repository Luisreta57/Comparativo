"""
Comparativo Q3 2026 vs Q3 2025 · BD
App Streamlit que renderiza la presentación HTML a pantalla completa.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Comparativo Q3 2026 vs Q3 2025 · BD",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Ocultar la interfaz de Streamlit para que solo se vea la presentación
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      .stApp {background: #1E1B5E;}
      iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_PATH = Path(__file__).parent / "presentacion.html"
html = HTML_PATH.read_text(encoding="utf-8")

# Altura del visor (px). Ajustable desde la URL: ?alto=900
alto = int(st.query_params.get("alto", 760))

components.html(html, height=alto, scrolling=False)

# Botón de descarga discreto al pie
st.download_button(
    "⬇️ Descargar presentación (HTML)",
    data=html,
    file_name="Comparativo_Q3_2026_vs_2025.html",
    mime="text/html",
)
