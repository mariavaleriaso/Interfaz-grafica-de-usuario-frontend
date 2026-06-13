# Dashboard Principal del Sistema de Predicción Bursátil Inteligente

Este proyecto implementa un dashboard interactivo utilizando Streamlit en Python, diseñado para Traders y Analistas Financieros. Permite visualizar datos de mercado en tiempo real (simulados) con gráficos de velas japonesas, indicadores técnicos y métricas clave.

## Características

*   **Gráfico de Velas Japonesas**: Visualización interactiva de datos OHLCV (Open, High, Low, Close, Volume) con `plotly.graph_objects`.
*   **Selectores de Activos**: Alterna entre 'Acciones' y 'Criptomonedas' mediante `st.radio`.
*   **Selección de Ticker y Período**: Elige entre tickers populares (AAPL, MSFT, GOOGL, TSLA, NVDA, BTC-USD, ETH-USD) y períodos de tiempo (1M, 3M, 6M, 1A, 2A, 5A) con `st.selectbox`.
*   **Indicadores Técnicos**: Superposición de medias móviles simples (SMA 20, SMA 50) y media móvil exponencial (EMA 12) calculadas con Pandas.
*   **Sub-gráfico de Volumen**: Muestra el volumen de negociación en un sub-gráfico integrado.
*   **Métricas Clave**: Visualización de precio actual, variación porcentual, volumen y capitalización de mercado en un diseño de columnas con `st.metric`.
*   **Datos Simulados**: Utiliza datos OHLCV simulados de forma realista con `numpy` y `pandas`, eliminando la necesidad de APIs externas para su funcionamiento inicial.
*   **Diseño Responsivo**: Configuración de página `layout=\'wide\'` para una experiencia de usuario óptima.

## Requisitos Previos

Asegúrate de tener Python 3.7 o superior instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

## Instalación

1.  **Clona este repositorio** (o descarga los archivos `app.py` y `README.md`):

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

    *(Nota: Si no tienes un repositorio, simplemente asegúrate de que `app.py` y `README.md` estén en el mismo directorio.)*

2.  **Instala las dependencias necesarias**:

    Abre tu terminal o línea de comandos y ejecuta el siguiente comando para instalar todas las librerías requeridas:

    ```bash
    pip install streamlit pandas numpy plotly
    ```

## Ejecución de la Aplicación

Una vez que hayas instalado las dependencias, puedes iniciar la aplicación Streamlit ejecutando el siguiente comando en tu terminal desde el directorio donde se encuentra `app.py`:

```bash
streamlit run app.py
```

Esto abrirá automáticamente el dashboard en tu navegador web predeterminado. Si no se abre, puedes acceder a él a través de la URL que se mostrará en tu terminal (generalmente `http://localhost:8501`).

## Estructura del Proyecto

*   `app.py`: El archivo principal de la aplicación Streamlit que contiene toda la lógica del dashboard.
*   `README.md`: Este archivo, que proporciona información sobre el proyecto y las instrucciones de uso.

## Contacto

Para cualquier pregunta o sugerencia, no dudes en contactar.
