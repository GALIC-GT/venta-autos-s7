import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.header('Análisis de anuncios de venta de coches')

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

# Lógica a ejecutar cuando se selecciona la casilla
if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Se crea un histograma utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Título del  gráfico
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Casilla para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

# Crear un scatter plot utilizando plotly.graph_objects
fig = go.Figure(
    data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

# Titulo del gráfico
fig.update_layout(title_text='Relación entre Odómetro y Precio')

# Mostrar el gráfico Plotly
st.plotly_chart(fig, use_container_width=True)
