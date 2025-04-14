import pandas as pd
import plotly.express as px
import streamlit as st

# Título principal de la aplicación
st.header('Explorador de Vehículos en Venta')

# Cargar el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Selección del objetivo del usuario
objetivo = st.radio(
    "¿Cuál es tu objetivo?",
    ["Comprar un vehículo", "Vender un vehículo"]
)

# Funciones comunes
if st.checkbox("Mostrar histograma de precios"):
    fig_price_hist = px.histogram(
        car_data,
        x='price',
        nbins=100,
        title='Distribución de precios de vehículos',
        labels={'price': 'Precio en USD', 'count': 'Número de vehículos'},
        color_discrete_sequence=['royalblue']
    )
    st.plotly_chart(fig_price_hist, use_container_width=True)

if st.button("Mostrar gráfico Precio vs. Kilometraje"):
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre Kilometraje y Precio",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio en USD"},
        opacity=0.5,
        color_discrete_sequence=["darkcyan"]
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Funcionalidades específicas por objetivo
if objetivo == "Comprar un vehículo":
    if st.checkbox("Mostrar boxplot de kilometraje por tipo de vehículo"):
        fig_box_odometer_type = px.box(
            car_data,
            x='type',
            y='odometer',
            title='Distribución del Kilometraje por Tipo de Vehículo',
            labels={
                'odometer': 'Kilometraje (millas)', 'type': 'Tipo de vehículo'},
            color_discrete_sequence=['teal']
        )
        st.plotly_chart(fig_box_odometer_type, use_container_width=True)

    if st.checkbox("Mostrar relación entre precio y condición"):
        fig_price_condition = px.box(
            car_data,
            x='condition',
            y='price',
            title='Relación entre Precio y Estado de Conservación',
            labels={'price': 'Precio en USD',
                    'condition': 'Condición del vehículo'},
            color_discrete_sequence=['indigo']
        )
        st.plotly_chart(fig_price_condition, use_container_width=True)

if objetivo == "Vender un vehículo":
    if st.checkbox("Mostrar días listados por tipo de vehículo"):
        fig_days_listed = px.box(
            car_data,
            x='type',
            y='days_listed',
            title='Días Listados por Tipo de Vehículo',
            labels={'days_listed': 'Días listados',
                    'type': 'Tipo de vehículo'},
            color_discrete_sequence=['crimson']
        )
        st.plotly_chart(fig_days_listed, use_container_width=True)

# Pie de página
st.markdown("""
---
**Aplicación creada para analizar y visualizar datos 
            de vehículos usados listados para su venta en EE.UU.**
""")
