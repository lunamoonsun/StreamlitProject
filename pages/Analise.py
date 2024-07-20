import streamlit as st
import plotly.express as px

st.header("Distribuição dos Dados")

if 'Dados' not in st.session_state:
    st.error("Por favor, carregue os dados primeiro.")
else:
   data = st.session_state['Dados']

   col1, col2 = st.columns(2)
   with col1:
       fig1 = px.histogram(data, x='VALOREMPENHO', title='Histograma do Valor de Empenho')
       st.plotly_chart(fig1, use_container_width=True)

       fig2 = px.box(data, x='VALOREMPENHO', title='Boxplot do Valor de Empenho')
       st.plotly_chart(fig2, use_container_width=True) 

   with col2:
       fig3 = px.histogram(data, x='PIB', title='Histograma do Valor do PIB')
       st.plotly_chart(fig3, use_container_width=True)

       fig4 = px.box(data, x='PIB', title='Boxplot do Valor do PIB')
       st.plotly_chart(fig4, use_container_width=True) 

   