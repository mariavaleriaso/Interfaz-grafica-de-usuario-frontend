import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Configuración
st.set_page_config(
    page_title="InvestAI • Panel de Trading",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    h1, h2, h3 { color: #1F3864; }
    .big-signal {
        font-size: 3.8rem;
        font-weight: 700;
        padding: 2rem 3rem;
        border-radius: 20px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .news-card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Datos de ejemplo
def load_data():
    signals = {
        "AAPL": {"signal": "COMPRA", "confidence": 0.87},
        "TSLA": {"signal": "VENTA", "confidence": 0.76},
        "GOOG": {"signal": "MANTENER", "confidence": 0.65}
    }
    
    market_sentiment = 68
    
    news_data = [
        {
            "title": "Apple presenta nuevos chips M4 con mejoras en IA",
            "time": "hace 12 min",
            "sentiment": 0.92,
            "impact": "Positivo"
        },
        {
            "title": "Tesla reduce precios en Europa ante competencia china",
            "time": "hace 45 min",
            "sentiment": 0.34,
            "impact": "Negativo"
        },
        {
            "title": "Google Cloud crece un 32% impulsado por IA generativa",
            "time": "hace 2 horas",
            "sentiment": 0.81,
            "impact": "Positivo"
        }
    ]
    return signals, market_sentiment, news_data

signals, market_sentiment, news_data = load_data()

# Sidebar
with st.sidebar:
    st.title("InvestAI")
    st.markdown("**Trading con Machine Learning**")
    asset = st.selectbox("Seleccionar Activo", ["AAPL", "TSLA", "GOOG"], index=0)
    st.divider()
    st.caption(datetime.now().strftime("%d %b %Y, %H:%M"))

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("📊 Panel de Señales Inteligentes")
    st.markdown("**Modelo SVM + Análisis de Sentimiento**")
with col2:
    st.metric("Precio Actual", "$226.84", "+1.24%")

st.divider()

# Contenido principal
col_signal, col_gauge = st.columns([1, 1])

# Señal SVM
with col_signal:
    st.subheader("🔍 Señal de Trading (SVM)")
    current = signals[asset]
    
    color_map = {"COMPRA": "#22c55e", "VENTA": "#ef4444", "MANTENER": "#eab308"}
    signal_color = color_map.get(current["signal"], "#64748b")
    
    st.markdown(f"""
    <div class="big-signal" style="background-color: {signal_color}15; color: {signal_color}; border: 4px solid {signal_color}">
        {current["signal"]}
    </div>
    """, unsafe_allow_html=True)
    
    st.metric("Confianza del Modelo", f"{current['confidence']*100:.1f}%")

# Gauge de Sentimiento
with col_gauge:
    st.subheader("📈 Sentimiento del Mercado")
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=market_sentiment,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Índice de Sentimiento (0-100)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#1F3864"},
            'steps': [
                {'range': [0, 40], 'color': "#fecaca"},
                {'range': [40, 60], 'color': "#fde047"},
                {'range': [60, 100], 'color': "#86efac"}
            ],
            'threshold': {'line': {'color': "#C5961A", 'width': 5}, 'value': market_sentiment}
        }
    ))
    
    fig.update_layout(height=340, margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig, use_container_width=True)

# Noticias
st.divider()
st.subheader("📰 Feed de Noticias Financieras")

for news in news_data:
    color = "#22c55e" if news["sentiment"] > 0.6 else "#ef4444" if news["sentiment"] < 0.4 else "#eab308"
    
    st.markdown(f"""
    <div class="news-card">
        <div style="display:flex; justify-content:space-between; align-items:start;">
            <div style="flex:1;">
                <p style="font-weight:600; margin:0; color:#1F3864;">{news["title"]}</p>
                <p style="color:#64748b; margin:6px 0 0 0; font-size:0.9rem;">{news["time"]}</p>
            </div>
            <div style="text-align:right;">
                <div style="background:{color}20; color:{color}; padding:4px 14px; border-radius:9999px; font-size:0.85rem; font-weight:600;">
                    {news["impact"]}
                </div>
                <p style="margin:8px 0 0 0; font-size:1.3rem; font-weight:700; color:{color}">
                    {news["sentiment"]*100:.0f}%
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("<p style='text-align:center; color:#64748b;'>InvestAI • Datos de ejemplo</p>", unsafe_allow_html=True)
