# Streamlit App
import streamlit as st

st.set_page_config(page_title='Trading Room Cibernético')
st.title('Trading Room Cibernético')

st.markdown('Bienvenido al Trading Room de Calle.')
st.markdown('Ticker: MNQ | MES | XAU/USD | EUR/USD | USD/CAD | USD/JPY | USD/CHF | GBP/USD')
st.markdown('Análisis IA vendrá aquí.')

# Bloomberg Live simulación (puedes reemplazar con tu m3u8 embed más adelante)
st.video('https://storage.googleapis.com/streamlit-examples/video.mp4')
