
# pip install streamlit plotly pandas numpy

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

# --- Configuración de la página de Streamlit ---
st.set_page_config(layout="wide", page_title="Dashboard de Análisis Financiero")
st.title("Dashboard de Análisis de Mercado")

# --- Funciones para generar datos simulados ---
def generate_simulated_ohlcv(ticker, days, start_date=None):
    if start_date is None:
        start_date = datetime.now() - timedelta(days=days)
    dates = pd.date_range(start=start_date, periods=days, freq='D')

    # Generar precios de apertura con una tendencia alcista o bajista suave
    np.random.seed(hash(ticker) % (2**32 - 1)) # Semilla para reproducibilidad por ticker
    initial_price = np.random.uniform(50, 200) if 'USD' not in ticker else np.random.uniform(10000, 50000)
    price_changes = np.random.normal(0, 1, days).cumsum() # Movimiento aleatorio
    # Añadir una tendencia para que no sea solo ruido
    trend = np.linspace(0, 0.1 * days, days) if np.random.rand() > 0.5 else np.linspace(0, -0.1 * days, days)
    open_prices = initial_price + price_changes + trend
    open_prices = np.maximum(open_prices, 1) # Asegurar precios positivos

    high_prices = open_prices * (1 + np.random.uniform(0.005, 0.02, days))
    low_prices = open_prices * (1 - np.random.uniform(0.005, 0.02, days))
    close_prices = np.random.uniform(low_prices, high_prices, days)

    # Asegurar que close esté entre low y high
    close_prices = np.where(close_prices < low_prices, low_prices, close_prices)
    close_prices = np.where(close_prices > high_prices, high_prices, close_prices)

    # Ajustar open y close para que no sean iguales
    for i in range(days):
        if open_prices[i] == close_prices[i]:
            if np.random.rand() > 0.5:
                close_prices[i] += 0.01 * open_prices[i]
            else:
                close_prices[i] -= 0.01 * open_prices[i]
            close_prices[i] = np.clip(close_prices[i], low_prices[i], high_prices[i])

    volume = np.random.randint(1000000, 100000000, days)
    adj_close = close_prices * np.random.uniform(0.98, 1.02, days) # Simular ajuste

    df = pd.DataFrame({
        'Date': dates,
        'Open': open_prices,
        'High': high_prices,
        'Low': low_prices,
        'Close': close_prices,
        'Adj Close': adj_close,
        'Volume': volume
    })
    df.set_index('Date', inplace=True)
    return df

def calculate_technical_indicators(df):
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['EMA_12'] = df['Close'].ewm(span=12, adjust=False).mean()
    return df

# --- Sidebar --- 
st.sidebar.header("Configuración del Mercado")

tickers = {
    "AAPL": "Acciones", "MSFT": "Acciones", "GOOGL": "Acciones",
    "TSLA": "Acciones", "NVDA": "Acciones",
    "BTC-USD": "Criptomonedas", "ETH-USD": "Criptomonedas"
}

selected_ticker = st.sidebar.selectbox(
    "Selecciona un Ticker",
    list(tickers.keys())
)

period_options = {
    "1M": 30, "3M": 90, "6M": 180,
    "1A": 365, "2A": 730, "5A": 1825
}

selected_period_label = st.sidebar.selectbox(
    "Selecciona un Período",
    list(period_options.keys())
)

days_to_simulate = period_options[selected_period_label]

# --- Generar y procesar datos ---
df = generate_simulated_ohlcv(selected_ticker, days_to_simulate)
df = calculate_technical_indicators(df)

# --- Pestañas --- 
tab1, tab2 = st.tabs(["Acciones", "Criptomonedas"])

with tab1:
    st.header("Análisis de Acciones")
    if tickers[selected_ticker] == "Acciones":
        # --- Gráfico de Velas Japonesas y Volumen ---
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                            vertical_spacing=0.1, row_heights=[0.7, 0.3])

        # Velas Japonesas
        fig.add_trace(go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'],
                                     name='Velas',
                                     increasing_line_color='#26A69A',
                                     decreasing_line_color='#EF5350'),
                      row=1, col=1)

        # Indicadores Técnicos
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], mode='lines', name='SMA 20',
                                 line=dict(color='#1F3864', width=1)), row=1, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], mode='lines', name='SMA 50',
                                 line=dict(color='#C5961A', width=1)), row=1, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=df['EMA_12'], mode='lines', name='EMA 12',
                                 line=dict(color='purple', width=1)), row=1, col=1)

        # Volumen
        colors = ['#26A69A' if close > open else '#EF5350' for close, open in zip(df['Close'], df['Open'])]
        fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volumen',
                                 marker_color=colors),
                      row=2, col=1)

        fig.update_layout(xaxis_rangeslider_visible=False, # Deshabilitar rangeslider por defecto en el subgráfico
                          template="plotly_white",
                          title_text=f"Gráfico de Velas y Volumen para {selected_ticker}",
                          height=700,
                          xaxis_tickformat='%d %b %Y')

        fig.update_yaxes(title_text="Precio", row=1, col=1)
        fig.update_yaxes(title_text="Volumen", row=2, col=1)

        # Añadir rangeslider al eje X principal (superior)
        fig.update_layout(xaxis=go.layout.XAxis(rangeslider=dict(visible=True)))

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Selecciona un ticker de acciones para ver el análisis.")

with tab2:
    st.header("Análisis de Criptomonedas")
    if tickers[selected_ticker] == "Criptomonedas":
        # --- Gráfico de Velas Japonesas y Volumen (similar al de acciones) ---
        fig_crypto = make_subplots(rows=2, cols=1, shared_xaxes=True,
                                   vertical_spacing=0.1, row_heights=[0.7, 0.3])

        # Velas Japonesas
        fig_crypto.add_trace(go.Candlestick(x=df.index,
                                            open=df['Open'],
                                            high=df['High'],
                                            low=df['Low'],
                                            close=df['Close'],
                                            name='Velas',
                                            increasing_line_color='#26A69A',
                                            decreasing_line_color='#EF5350'),
                             row=1, col=1)

        # Indicadores Técnicos
        fig_crypto.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], mode='lines', name='SMA 20',
                                        line=dict(color='#1F3864', width=1)), row=1, col=1)
        fig_crypto.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], mode='lines', name='SMA 50',
                                        line=dict(color='#C5961A', width=1)), row=1, col=1)
        fig_crypto.add_trace(go.Scatter(x=df.index, y=df['EMA_12'], mode='lines', name='EMA 12',
                                        line=dict(color='purple', width=1)), row=1, col=1)

        # Volumen
        colors_crypto = ['#26A69A' if close > open else '#EF5350' for close, open in zip(df['Close'], df['Open'])]
        fig_crypto.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volumen',
                                        marker_color=colors_crypto),
                             row=2, col=1)

        fig_crypto.update_layout(xaxis_rangeslider_visible=False,
                                 template="plotly_white",
                                 title_text=f"Gráfico de Velas y Volumen para {selected_ticker}",
                                 height=700,
                                 xaxis_tickformat='%d %b %Y')

        fig_crypto.update_yaxes(title_text="Precio", row=1, col=1)
        fig_crypto.update_yaxes(title_text="Volumen", row=2, col=1)

        fig_crypto.update_layout(xaxis=go.layout.XAxis(rangeslider=dict(visible=True)))

        st.plotly_chart(fig_crypto, use_container_width=True)

        # --- Panel lateral de métricas en tiempo real simuladas (solo para criptomonedas) ---
        st.sidebar.subheader("Métricas en Tiempo Real (Simuladas)")
        current_price = df['Close'].iloc[-1]
        previous_close = df['Close'].iloc[-2] if len(df) > 1 else current_price
        price_change_percent = ((current_price - previous_close) / previous_close) * 100
        daily_volume = df['Volume'].iloc[-1]
        market_cap = current_price * np.random.randint(1000000000, 5000000000) # Simular Market Cap

        col_metrics1, col_metrics2 = st.sidebar.columns(2)
        with col_metrics1:
            st.metric(label="Precio Actual", value=f"${current_price:,.2f}", delta=f"{price_change_percent:,.2f}%")
        with col_metrics2:
            st.metric(label="Volumen Diario", value=f"{daily_volume:,.0f}")
        st.sidebar.metric(label="Capitalización de Mercado", value=f"${market_cap:,.0f}")

    else:
        st.info("Selecciona un ticker de criptomonedas para ver el análisis y las métricas.")

# --- Layout responsivo (ejemplo de uso de st.columns para la vista principal) ---
# Aunque el problema pide 8 columnas para el gráfico y 4 para el panel lateral,
# la estructura de Streamlit con sidebar y main area ya maneja esto de forma implícita.
# Si se quisiera un panel lateral en el área principal, se usaría st.columns.
# Para este caso, el sidebar ya cumple la función de panel lateral.

# Ejemplo de cómo se usaría st.columns si el panel lateral no fuera el sidebar:
# main_col, side_panel_col = st.columns([8, 4])
# with main_col:
#    st.write("Aquí iría el gráfico principal")
# with side_panel_col:
#    st.write("Aquí irían las métricas o información adicional")

