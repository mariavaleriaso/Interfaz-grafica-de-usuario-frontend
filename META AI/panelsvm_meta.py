import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Configuración de página
st.set_page_config(
    page_title="InvestAI - Panel ML",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS custom para paleta y tipografía
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

   .main {
        background-color: #F8FAFC;
    }

   .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }

    h1 {
        color: #1F3864!important;
        font-weight: 700!important;
    }

   .stSelectbox label {
        color: #1F3864!important;
        font-weight: 600!important;
    }

    /* Badge de señal */
   .signal-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 20px 48px;
        border-radius: 16px;
        font-size: 28px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin: 16px 0;
    }

   .signal-compra {
        background: linear-gradient(135deg, #10B981, #059669);
        color: white;
    }

   .signal-venta {
        background: linear-gradient(135deg, #EF4444, #DC2626);
        color: white;
    }

   .signal-mantener {
        background: linear-gradient(135deg, #6B7280, #4B5563);
        color: white;
    }

    /* Cards */
   .custom-card {
        background: white;
        border-radius: 16px;
        padding: 28px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    /* News items */
   .news-item {
        background: white;
        border-radius: 12px;
        padding: 18px;
        border-left: 4px solid #1F3864;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

   .news-title {
        font-weight: 600;
        color: #0F172A;
        margin-bottom: 6px;
        font-size: 15px;
    }

   .news-meta {
        font-size: 13px;
        color: #64748B;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

   .sentiment-badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }

   .sent-pos { background: rgba(16, 185, 129, 0.15); color: #059669; }
   .sent-neg { background: rgba(239, 68, 68, 0.15); color: #DC2626; }
   .sent-neu { background: rgba(107, 114, 128, 0.15); color: #4B5563; }
</style>
""", unsafe_allow_html=True)

# DATOS DE EJEMPLO PRECARGADOS
MOCK_DATA = {
    "AAPL": {
        "signal": "COMPRA",
        "signal_confidence": 0.78,
        "sentiment": 72,
        "news": [
            {"title": "Apple supera expectativas en ingresos de iPhone Q4", "source": "Bloomberg", "time": "Hace 2h", "score": 0.82},
            {"title": "Analistas elevan precio objetivo de AAPL tras evento Vision Pro", "source": "Reuters", "time": "Hace 5h", "score": 0.67},
            {"title": "Preocupaciones por demanda en China afectan a Apple", "source": "WSJ", "time": "Hace 8h", "score": -0.31}
        ]
    },
    "TSLA": {
        "signal": "MANTENER",
        "signal_confidence": 0.54,
        "sentiment": 48,
        "news": [
            {"title": "Tesla recorta precios en Europa para impulsar ventas", "source": "CNBC", "time": "Hace 1h", "score": -0.15},
            {"title": "Producción de Cybertruck alcanza nuevo récord mensual", "source": "TechCrunch", "time": "Hace 4h", "score": 0.58},
            {"title": "Investigación de NHTSA sobre Autopilot genera incertidumbre", "source": "Reuters", "time": "Hace 6h", "score": -0.42}
        ]
    },
    "GOOG": {
        "signal": "VENTA",
        "signal_confidence": 0.71,
        "sentiment": 34,
        "news": [
            {"title": "Google enfrenta nueva demanda antimonopolio en EE.UU.", "source": "NYT", "time": "Hace 3h", "score": -0.68},
            {"title": "Gemini AI de Google gana cuota vs ChatGPT según estudio", "source": "The Verge", "time": "Hace 5h", "score": 0.44},
            {"title": "Ingresos por publicidad de YouTube caen 3% interanual", "source": "Bloomberg", "time": "Hace 7h", "score": -0.52}
        ]
    }
}

# HEADER
col_logo, col_selector = st.columns([3, 1])
with col_logo:
    st.markdown("""
    <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 8px;'>
        <div style='width: 40px; height: 40px; border-radius: 12px; background: linear-gradient(135deg, #1F3864, #C5961A);
                    display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 18px;'>AI</div>
        <h1 style='margin: 0;'>Invest<span style='color: #C5961A;'>AI</span></h1>
    </div>
    <p style='color: #64748B; margin-top: -8px;'>Panel de Machine Learning - SVM + Análisis de Sentimiento</p>
    """, unsafe_allow_html=True)

with col_selector:
    asset = st.selectbox("Activo", ["AAPL", "TSLA", "GOOG"], index=0)

data = MOCK_DATA[asset]

# COMPONENTE 1: SEÑAL SVM + COMPONENTE 2: GAUGE SENTIMIENTO
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.markdown("### Señal de Trading - SVM")

    # Determinar clase CSS según señal
    signal_class = f"signal-{data['signal'].lower()}"
    st.markdown(f"<div class='signal-badge {signal_class}'>{data['signal']}</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style='margin-top: 16px;'>
        <div style='display: flex; justify-content: space-between; margin-bottom: 8px;'>
            <span style='color: #64748B; font-size: 14px;'>Confianza del modelo</span>
            <span style='color: #1F3864; font-weight: 600; font-size: 14px;'>{data['signal_confidence']*100:.0f}%</span>
        </div>
        <div style='background: #E2E8F0; border-radius: 8px; height: 8px; overflow: hidden;'>
            <div style='background: linear-gradient(90deg, #1F3864, #C5961A); height: 100%; width: {data['signal_confidence']*100}%; transition: width 0.3s;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.markdown("### Sentimiento de Mercado")

    # Gauge con Plotly
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=data['sentiment'],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "", 'font': {'size': 14}},
        number={'suffix': "", 'font': {'size': 36, 'color': '#1F3864', 'family': 'Inter'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#64748B"},
            'bar': {'color': "#1F3864", 'thickness': 0.25},
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
                {'range': [0, 33], 'color': 'rgba(239, 68, 68, 0.2)'},
                {'range': [33, 66], 'color': 'rgba(107, 114, 128, 0.2)'},
                {'range': [66, 100], 'color': 'rgba(16, 185, 129, 0.2)'}
            ],
            'threshold': {
                'line': {'color': "#C5961A", 'width': 4},
                'thickness': 0.75,
                'value': data['sentiment']
            }
        }
    ))

    fig.update_layout(
        height=260,
        margin=dict(l=20, r=20, t=40, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Inter', 'color': '#64748B'}
    )

    st.plotly_chart(fig, use_container_width=True)

    # Etiqueta de sentimiento
    if data['sentiment'] >= 66:
        sent_label, sent_color = "Positivo", "#10B981"
    elif data['sentiment'] >= 33:
        sent_label, sent_color = "Neutral", "#6B7280"
    else:
        sent_label, sent_color = "Negativo", "#EF4444"

    st.markdown(f"""
    <div style='text-align: center; margin-top: -20px;'>
        <span style='background: {sent_color}20; color: {sent_color}; padding: 6px 16px;
                     border-radius: 20px; font-weight: 600; font-size: 14px;'>{sent_label}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# COMPONENTE 3: FEED DE NOTICIAS
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### Feed de Noticias Financieras")

for news in data['news']:
    # Determinar clase de sentimiento
    if news['score'] > 0.2:
        sent_class, sent_text = "sent-pos", f"+{news['score']:.2f}"
    elif news['score'] < -0.2:
        sent_class, sent_text = "sent-neg", f"{news['score']:.2f}"
    else:
        sent_class, sent_text = "sent-neu", f"{news['score']:.2f}"

    st.markdown(f"""
    <div class='news-item'>
        <div class='news-title'>{news['title']}</div>
        <div class='news-meta'>
            <span>{news['source']} · {news['time']}</span>
            <span class='sentiment-badge {sent_class}'>Sentimiento: {sent_text}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #94A3B8; font-size: 13px; padding: 20px;'>
    InvestAI © 2026 · Modelo SVM + LSTM · Datos actualizados: {}
</div>
""".format(datetime.now().strftime("%d/%m/%Y %H:%M")), unsafe_allow_html=True)