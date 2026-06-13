import { createFileRoute } from "@tanstack/react-router";
import { Link } from "@tanstack/react-router";
import { AppShell } from "@/components/AppShell";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "InvestAI — Sistema Inteligente de Inversión" },
      { name: "description", content: "16 modelos de IA para predicción bursátil: SVM, LSTM, XGBoost, GRU, NLP y más." },
      { property: "og:title", content: "InvestAI — Sistema Inteligente de Inversión" },
      { property: "og:description", content: "Plataforma de decisiones de inversión con IA." },
    ],
  }),
  component: Index,
});

const MODULES = [
  { to: "/dashboard", icon: "📊", title: "Dashboard Completo", desc: "Vista integrada de mercado, predicciones, señales y backtesting." },
  { to: "/mercado", icon: "📈", title: "Datos de Mercado", desc: "Candlestick con SMA, EMA y volumen en tiempo real." },
  { to: "/svm", icon: "🎯", title: "SVM Clasificación", desc: "Señales BUY/SELL/HOLD con SVC kernel RBF." },
  { to: "/lstm", icon: "🔮", title: "LSTM Pronóstico", desc: "Predicción continua de precios con banda de confianza." },
  { to: "/nlp", icon: "📰", title: "NLP Sentimiento", desc: "Análisis VADER + GPT-4o sobre noticias financieras." },
  { to: "/estrategias", icon: "♟️", title: "Estrategias", desc: "Covered Call, Iron Condor y más con payoff interactivo." },
  { to: "/portafolio", icon: "💼", title: "Portafolio", desc: "Posiciones, equity y métricas de backtesting." },
  { to: "/broker", icon: "⚡", title: "Broker IBKR", desc: "Envío de órdenes a Interactive Brokers." },
  { to: "/auth", icon: "👤", title: "Autenticación", desc: "Inicio de sesión, registro y recuperación." },
] as const;

function Index() {
  return (
    <AppShell title="InvestAI — Inicio">
      <section className="bg-gradient-to-br from-[#1F3864] to-[#16294a] px-4 py-10 text-white sm:px-8 sm:py-14">
        <div className="mx-auto max-w-6xl">
          <span className="inline-block rounded-full bg-[#C5961A] px-3 py-1 text-xs font-bold uppercase tracking-wide">
            Sistema Web · IA Generativa
          </span>
          <h1 className="mt-4 text-3xl font-black leading-tight sm:text-5xl">
            Decisiones de inversión <span className="text-[#C5961A]">impulsadas por IA</span>
          </h1>
          <p className="mt-3 max-w-2xl text-sm text-white/80 sm:text-base">
            16 modelos predictivos (SVC, LSTM, XGBoost, GRU, NLP VADER, GPT-4o, ARIMA-LSTM y
            ensamblados) integrados con Yahoo Finance, CoinMarketCap e Interactive Brokers.
          </p>
          <div className="mt-6 flex flex-wrap gap-3">
            <Link
              to="/dashboard"
              className="rounded-md bg-[#C5961A] px-5 py-2.5 text-sm font-bold text-white hover:bg-[#a87f15]"
            >
              ▶ Abrir Dashboard
            </Link>
            <Link
              to="/auth"
              className="rounded-md border border-white/30 bg-white/10 px-5 py-2.5 text-sm font-bold text-white hover:bg-white/20"
            >
              Iniciar Sesión
            </Link>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-4 py-8 sm:px-8">
        <h2 className="mb-4 text-lg font-bold text-[#1F3864] sm:text-xl">Módulos del Sistema</h2>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {MODULES.map((m) => (
            <Link
              key={m.to}
              to={m.to}
              className="group flex flex-col rounded-xl border bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:shadow-lg"
            >
              <div className="mb-3 grid h-11 w-11 place-items-center rounded-lg bg-[#f0f3f8] text-2xl">
                {m.icon}
              </div>
              <h3 className="text-base font-bold text-[#1F3864] group-hover:text-[#C5961A]">
                {m.title}
              </h3>
              <p className="mt-1 text-sm text-gray-600">{m.desc}</p>
            </Link>
          ))}
        </div>
      </section>
    </AppShell>
  );
}
