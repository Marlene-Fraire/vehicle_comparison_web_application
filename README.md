# Vehicle Comparison Web Application 🚗📊

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar una aplicación web interactiva que permita analizar, comparar y visualizar datos de vehículos usados listados para su venta en EE.UU. La aplicación está pensada tanto para compradores como para vendedores, proporcionando herramientas que les ayuden a tomar decisiones más informadas basadas en los datos.

Se utilizó un enfoque de análisis exploratorio de datos (EDA) para identificar patrones, relaciones clave y comportamientos relevantes en variables como precio, kilometraje, condición del vehículo, tipo, color y transmisión.

## Objetivos de la App

**Para compradores**  
- Explorar modelos con menor kilometraje.
- Analizar la relación entre precio y condición del vehículo.
- Estimar el valor aproximado según características seleccionadas.

**Para vendedores**  
- Estimar el tiempo promedio de venta según tipo de vehículo.
- Comprender cómo factores como el kilometraje, condición o tipo afectan el valor de mercado.
- Evaluar el impacto de la pintura o transmisión sobre la demanda.

## Tecnologías Utilizadas

- Python
- pandas
- plotly.express
- Streamlit
- Jupyter Notebook

## Estructura del Repositorio

```
vehicle_comparison_web_application/
├── app.py               # Código de la app en Streamlit
├── vehicles_us.csv      # Dataset original
├── requirements.txt     # Librerías necesarias
├── README.md            # Este archivo
├── .streamlit/
│   └── config.toml      # Configuración para Render
└── notebooks/
    └── EDA.ipynb        # Análisis exploratorio de datos
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

## Despliegue

La aplicación está desplegada en Render y puede ser accedida desde: [🔗 Enlace a la App](https://<tu-nombre-de-app>.onrender.com)

---

¡Gracias por visitar este repositorio! Esperamos que esta app te sea útil para analizar el mercado de autos usados.