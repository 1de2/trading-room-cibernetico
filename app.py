# Streamlit App
import streamlit as st

st.set_page_config(page_title='Trading Room Cibernético')
st.title('Trading Room Cibernético')

st.markdown('Bienvenido al Trading Room de Calle.')
st.markdown('Ticker: MNQ | MES | XAU/USD | EUR/USD | USD/CAD | USD/JPY | USD/CHF | GBP/USD')
st.markdown('Análisis IA vendrá aquí.')

# Bloomberg Live simulación (puedes reemplazar con tu m3u8 embed más adelante)
st.markdown("""
<video width="100%" height="500" controls autoplay muted>
  <source src="https://player-api.new.livestream.com/accounts/19720656/events/8791751/live.m3u8" type="application/x-mpegURL">
  Tu navegador no soporta video en vivo.
</video>
""", unsafe_allow_html=True)

