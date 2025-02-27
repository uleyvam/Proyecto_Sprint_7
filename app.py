import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# crear un encabezado
st.header('Gráficos de datos de anuncios de automóviles👽')

# crear una casilla de verificación
build_sample_data = st.checkbox('Mostrar una muestra de los datos')
build_histogram = st.checkbox(
    'Construir un histograma para la variable odometer (kilometraje)')
build_scatter = st.checkbox(
    'Construir un gráfico de dispersión para las columnas price (precio) y odometer')

if build_sample_data:  # si la casilla de verificación está seleccionada
    # crear una muestra de los datos
    sample = car_data.sample(10)
    # mostrar una tabla con la muestra de 10 filas
    st.write(sample)

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
