import streamlit as st

st.set_page_config(page_title="Trading Room Cibernético", layout="wide")
st.title("📈 Trading Room Cibernético")

# Layout principal
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Análisis IA")
    st.markdown("Aquí irá el análisis automático basado en eventos macroeconómicos y divergencias fundamentales.")
    st.markdown("📅 Noticias cargadas desde Forex Factory (por integrar scraping).")
    st.markdown("🧠 IA: Resumen diario macro vendrá aquí.")
    st.markdown("---")
    st.subheader("Ticker en tiempo real")
    st.markdown("MNQ | MES | XAU/USD | EUR/USD | USD/CAD | USD/JPY | USD/CHF | GBP/USD")

with col2:
    st.subheader("🔴 Bloomberg Live TV")
    st.markdown("""
    <video width="100%" height="300" controls autoplay muted>
        <source src="https://phoenix-lh.akamaihd.net/i/US01@500985/master.m3u8" type="application/x-mpegURL">
        Tu navegador no soporta video en vivo.
    </video>
    """, unsafe_allow_html=True)

# Navegación entre salas
st.markdown("---")
st.subheader("Salas de Trading")
salas = ["Sala NQ", "Sala FX", "Sala Commodities", "Sala Macro"]
selected = st.selectbox("Selecciona una sala para ver el stream:", salas)
st.success(f"🔗 Mostrando contenido de {selected} (simulado).")
st.video("https://www.youtube.com/watch?v=5qap5aO4i9A")
