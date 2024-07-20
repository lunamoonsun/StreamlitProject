import streamlit as st

st.header("Resumo dos Dados")

if 'Dados' not in st.session_state:
    st.error("Por favor, carregue os dados primeiro.")
else:
   data = st.session_state['Dados'].describe().reset_index()
   st.write(data)
   