import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# crear un encabezado
st.header('Gráficos de datos de anuncios de automóviles')

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:  # si la casilla de verificación está seleccionada
    # crear un histograma
    fig_1 = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_1, use_container_width=True)

if build_scatter:
    # crear un gráfico de dispersión
    fig_2 = px.scatter(car_data, x='odometer', y='price')
    # mostrar un gráfico de Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
