import streamlit as st
from st_aggrid import AgGrid

st.header("Visualização de Dados")

if 'Dados' not in st.session_state:
    st.error("Por favor, carregue os dados primeiro.")
else:
   top_n = st.session_state.get('top_n', 10)
   data = st.session_state['Dados']
   data_filtrados = data.head(top_n)
   AgGrid(data_filtrados, fit_columns_on_grid_load=True)