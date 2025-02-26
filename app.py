import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

# crear un histograma
fig_1 = px.histogram(car_data, x="odometer")

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig_1, use_container_width=True)

# crear un gráfico de dispersión
fig_2 = px.scatter(car_data, x='odometer', y='price')

# mostrar un gráfico de Plotly interactivo
st.plotly_chart(fig_2, use_container_width=True)
