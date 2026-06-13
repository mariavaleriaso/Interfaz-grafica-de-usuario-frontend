
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime

# Configuración de la página
st.set_page_config(layout='wide', page_title='Dashboard Bursátil Inteligente')

st.title('Dashboard Principal del Sistema de Predicción Bursátil Inteligente')

# --- Funciones para simular datos ---
def simulate_ohlcv(ticker, days, start_date=None):
    if start_date is None:
        start_date = datetime.date.today() - datetime.timedelta(days=days)
    dates = pd.date_range(start=start_date, periods=days, freq='D')
    
    # Simular precios de apertura, cierre, máximo y mínimo
    np.random.seed(42) # Para reproducibilidad
    open_price = 100 + np.cumsum(np.random.randn(days)) * 0.5
    close_price = open_price + np.random.randn(days) * 2
    high_price = np.maximum(open_price, close_price) + np.abs(np.random.randn(days)) * 1
    low_price = np.minimum(open_price, close_price) - np.abs(np.random.randn(days)) * 1
    
    # Asegurarse de que low <= open, close <= high
    low_price = np.minimum(low_price, np.minimum(open_price, close_price))
    high_price = np.maximum(high_price, np.maximum(open_price, close_price))

    volume = np.random.randint(1_000_000, 10_000_000, days)
    
    df = pd.DataFrame({
        'Date': dates,
        'Open': open_price,
        'High': high_price,
        'Low': low_price,
        'Close': close_price,
        'Volume': volume
    })
    df.set_index('Date', inplace=True)
    return df

# --- Sidebar para controles ---
st.sidebar.header('Controles del Dashboard')

asset_type = st.sidebar.radio(
    'Selecciona Tipo de Activo:',
    ('Acciones', 'Criptomonedas')
)

if asset_type == 'Acciones':
    ticker_options = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'NVDA']
else:
    ticker_options = ['BTC-USD', 'ETH-USD']

ticker = st.sidebar.selectbox('Selecciona Ticker:', ticker_options)

period_map = {
    '1M': 30,
    '3M': 90,
    '6M': 180,
    '1A': 365,
    '2A': 730,
    '5A': 1825
}
period_label = st.sidebar.selectbox('Selecciona Período:', list(period_map.keys()), index=1) # Default a 3M
days = period_map[period_label]

# --- Generar datos simulados ---
df = simulate_ohlcv(ticker, days)

# --- Cálculo de Indicadores Técnicos ---
df['SMA_20'] = df['Close'].rolling(window=20).mean()
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['EMA_12'] = df['Close'].ewm(span=12, adjust=False).mean()

# --- Creación del Gráfico de Velas Japonesas y Volumen ---
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                    vertical_spacing=0.1, 
                    row_heights=[0.7, 0.3])

# Gráfico de Velas Japonesas
fig.add_trace(go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name='Velas',
    increasing_line_color='#26A69A', # Verde para velas alcistas
    decreasing_line_color='#EF5350'  # Rojo para velas bajistas
), row=1, col=1)

# Indicadores Técnicos
fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], mode='lines', name='SMA 20', line=dict(color='blue', width=1)), row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], mode='lines', name='SMA 50', line=dict(color='orange', width=1)), row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df['EMA_12'], mode='lines', name='EMA 12', line=dict(color='purple', width=1)), row=1, col=1)

# Sub-gráfico de Volumen
fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volumen', marker_color='rgba(0,0,255,0.5)'), row=2, col=1)

# Actualizar layout del gráfico
fig.update_layout(
    xaxis_rangeslider_visible=False, # Ocultar el rango de fechas inferior
    title_text=f'Gráfico de Velas y Volumen para {ticker}',
    height=700,
    hovermode='x unified'
)

fig.update_yaxes(title_text='Precio', row=1, col=1)
fig.update_yaxes(title_text='Volumen', row=2, col=1)

# --- Métricas en columnas ---
st.subheader('Métricas Clave')

# Calcular métricas (usando los últimos datos disponibles)
latest_close = df['Close'].iloc[-1]
previous_close = df['Close'].iloc[-2] if len(df) > 1 else latest_close

price_change = latest_close - previous_close
percentage_change = (price_change / previous_close) * 100 if previous_close != 0 else 0

latest_volume = df['Volume'].iloc[-1]

# Simular Market Cap (ejemplo simple)
# Un valor base + variación aleatoria, para que sea diferente para acciones y criptos
if asset_type == 'Acciones':
    market_cap = (latest_close * 1_000_000_000) + (np.random.rand() * 10_000_000_000)
else: # Criptomonedas
    market_cap = (latest_close * 100_000_000) + (np.random.rand() * 1_000_000_000)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label=f'Precio Actual ({ticker})', value=f'${latest_close:.2f}')
with col2:
    st.metric(label='Variación % (Último Día)', value=f'{percentage_change:.2f}%', delta=f'{price_change:.2f}')
with col3:
    st.metric(label='Volumen (Último Día)', value=f'{latest_volume:,.0f}')
with col4:
    st.metric(label='Capitalización de Mercado', value=f'${market_cap:,.0f}')

# Mostrar el gráfico
st.plotly_chart(fig, use_container_width=True)
