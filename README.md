# Explorador de Vehículos en Venta

Esta aplicación web fue desarrollada para ofrecer visualizaciones interactivas que ayudan tanto a compradores como a vendedores de autos usados a tomar decisiones informadas.

---

## Objetivo de la aplicación

Ofrecer una herramienta interactiva que permita:

- Visualizar tendencias clave en los datos de vehículos usados listados para la venta.
- Explorar relaciones entre características como precio, kilometraje, tipo de vehículo y condición.
- Brindar orientación específica según si el usuario desea **comprar** o **vender** un automóvil.

---

## Funcionalidades principales

### Funciones comunes para todos los usuarios:
- Histograma de precios
- Dispersión de precios vs. kilometraje

### Para compradores:
- Boxplot de kilometraje por tipo de vehículo
- Relación entre precio y estado de conservación

### Para vendedores:
- Días listados por tipo de vehículo

---

## Estructura del Repositorio

```
vehicle_comparison_web_application/
├── app.py               # Código de la app en Streamlit
├── vehicles_us.csv      # Dataset original
├── requirements.txt     # Librerías necesarias
├── README.md            # Este archivo
├── .streamlit/
│   └── config.toml      # Configuración para Render
└── EDA.ipynb        # Análisis exploratorio de datos

---

## Requisitos

- Python 3.x
- Streamlit
- Plotly Express
- Pandas

```

## Cómo ejecutar el proyecto localmente

1. Crea y activa un entorno virtual:
   ```bash
   conda create -n vehicles_env python=3.11 -y
   conda activate vehicles_env
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## Acceso a la Aplicación Web
Puedes acceder a la versión desplegada de esta aplicación en el siguiente enlace: https://vehicle-comparison-web-application.onrender.com

---

¡Gracias por visitar este repositorio! Esperamos que esta app te sea útil para analizar el mercado de autos usados.