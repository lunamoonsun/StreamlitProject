import streamlit as st
import plotly.express as px

st.header("Maiores Valores")

if 'Dados' not in st.session_state:
    st.error("Por favor, carregue os dados primeiro.")
else:
    top_n = st.session_state.get('top_n', 10)
    data = st.session_state['Dados']

    col1, col2, col3 = st.columns(3)

    with col1:
        Mempenho = data.nlargest(top_n, 'VALOREMPENHO')
        fig = px.bar(Mempenho, x="MUNICIPIO", y="VALOREMPENHO", title='Maiores Empenhos')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        Mpibs = data.nlargest(top_n, 'PIB')
        fig = px.pie(Mpibs, values='PIB', names='MUNICIPIO', title='Maiores PIBs')
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        Mprop = data.nlargest(top_n, 'PROPORCAO')
        fig = px.bar(Mprop, x="MUNICIPIO", y="PROPORCAO", title='Maiores Gastos em Proporções ao PIB')
        st.plotly_chart(fig, use_container_width=True)