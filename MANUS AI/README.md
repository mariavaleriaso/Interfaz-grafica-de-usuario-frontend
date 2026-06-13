# Dashboard de Análisis Financiero con Inteligencia Artificial

Este proyecto es un prototipo de **Sistema Web de Apoyo en Decisiones de Inversión** desarrollado en Python utilizando **Streamlit**. La aplicación permite visualizar datos de mercado (acciones y criptomonedas) mediante gráficos de velas japonesas, indicadores técnicos y métricas en tiempo real, utilizando datos simulados realistas.

## 🚀 Características

- **Visualización Avanzada**: Gráficos de velas japonesas (Candlestick) interactivos con Plotly.
- **Indicadores Técnicos**: Cálculo dinámico de Medias Móviles Simples (SMA 20, SMA 50) y Media Móvil Exponencial (EMA 12).
- **Análisis de Volumen**: Subgráfico integrado con codificación de colores por tendencia.
- **Interactividad Total**: Selectores de activos (AAPL, MSFT, BTC, etc.) y períodos (1M a 5A) con re-renderizado automático.
- **Métricas en Tiempo Real**: Panel lateral con variaciones porcentuales y capitalización de mercado para criptoactivos.
- **Diseño Profesional**: Paleta de colores optimizada para analistas financieros y traders.

## 🛠️ Requisitos Previos

Asegúrate de tener instalado **Python 3.8** o superior en tu sistema. No se requieren claves de API externas, ya que el sistema utiliza un motor de simulación de datos OHLCV integrado.

## 📦 Instalación

1. **Clonar o descargar el repositorio**:
   Descarga el archivo `dashboard_financiero.py` en una carpeta local.

2. **Instalar dependencias**:
   Abre una terminal en la carpeta del proyecto y ejecuta el siguiente comando para instalar las librerías necesarias:
   ```bash
   pip install streamlit plotly pandas numpy
   ```

## 💻 Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando en tu terminal:

```bash
streamlit run dashboard_financiero.py
```

Una vez ejecutado, Streamlit abrirá automáticamente una pestaña en tu navegador predeterminado (usualmente en `http://localhost:8501`).

## 📖 Guía de Uso

1. **Panel Lateral (Sidebar)**:
   - Selecciona el **Ticker** del activo que deseas analizar.
   - Elige el **Período** de tiempo para la simulación de datos.
   - Observa las **Métricas en Tiempo Real** (disponibles especialmente para criptomonedas).

2. **Área Principal**:
   - Navega entre las pestañas **"Acciones"** y **"Criptomonedas"** según el activo seleccionado.
   - Interactúa con el gráfico: usa el **zoom**, el **pan** y el **rangeslider** inferior para explorar períodos específicos.
   - Pasa el cursor sobre las velas para ver los detalles de OHLCV y el valor de los indicadores técnicos.

## 🛠️ Tecnologías Utilizadas

- **Streamlit**: Framework para la creación de aplicaciones web de datos.
- **Plotly**: Librería de gráficos interactivos de alta calidad.
- **Pandas & NumPy**: Procesamiento de datos y cálculos matemáticos/financieros.

---
*Desarrollado como prototipo para Sistemas de Apoyo a Decisiones Financieras.*
