import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')
print(car_data.head())

st.header('INFORMACION DE VEHICULOS')

build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # Obtener todas las marcas únicas
    marcas_unicas = car_data['model'].unique()

    # Añadir una opción para seleccionar todas las marcas
    marcas_unicas = ['Todas las marcas'] + list(marcas_unicas)

    # Casillas de verificación para seleccionar las marcas
    marcas_seleccionadas = st.multiselect(
        'Selecciona los modelos:', marcas_unicas, key='histogram_multiselect')

    # Filtrar el conjunto de datos según las marcas seleccionadas
    if 'Todas las marcas' in marcas_seleccionadas:
        car_data_filtrado = car_data.copy()
    else:
        car_data_filtrado = car_data[car_data['model'].isin(
            marcas_seleccionadas)]

    # Crear un histograma para odómetros basado en las marcas seleccionadas
    fig = px.histogram(car_data_filtrado, x='odometer',
                       title='Histograma por odómetro y marca',
                       labels={'odometer': 'Odómetro', 'model': 'Marca'})
    st.plotly_chart(fig, use_container_width=True)


if build_scatter:  # si la casilla de verificación está seleccionada
    st.write('Construir un diagrama de dispersión para la columna odómetro')
    # Obtener todas las marcas únicas
    marcas_s_unicas = car_data['model'].unique()

    # Añadir una opción para seleccionar todas las marcas
    marcas_s_unicas = ['Todas las marcas'] + list(marcas_s_unicas)

    # Casillas de verificación para seleccionar las marcas
    marcas_seleccionadas_sc = st.multiselect(
        'Selecciona los modelos:', marcas_s_unicas, key='scatter_multiselect')

    # Filtrar el conjunto de datos según las marcas seleccionadas
    if 'Todas las marcas' in marcas_seleccionadas_sc:
        car_data_filtrado_sc = car_data.copy()
    else:
        car_data_filtrado_sc = car_data[car_data['model'].isin(
            marcas_seleccionadas_sc)]

    # Crear un diagrama de dispersión para odómetros basado en las marcas seleccionadas y en el precio
    fig = px.scatter(car_data_filtrado_sc, x='odometer', y='price', title='Dispersión por odómetro y marca',
                     labels={'odometer': 'Odómetro', 'model': 'Marca', 'price': 'Precio'}, color_discrete_sequence=['aquamarine'])
    st.plotly_chart(fig, use_container_width=True)
