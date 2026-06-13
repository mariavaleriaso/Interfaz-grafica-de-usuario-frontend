import { Link, useRouterState } from "@tanstack/react-router";
import { useState, type ReactNode } from "react";

const NAV = [
  { to: "/", label: "Inicio", icon: "🏠" },
  { to: "/dashboard", label: "Dashboard", icon: "📊" },
  { to: "/mercado", label: "Mercado", icon: "📈" },
  { to: "/svm", label: "SVM", icon: "🎯" },
  { to: "/lstm", label: "LSTM", icon: "🔮" },
  { to: "/nlp", label: "NLP", icon: "📰" },
  { to: "/estrategias", label: "Estrategias", icon: "♟️" },
  { to: "/portafolio", label: "Portafolio", icon: "💼" },
  { to: "/broker", label: "Broker", icon: "⚡" },
  { to: "/auth", label: "Cuenta", icon: "👤" },
] as const;

export function AppShell({ children, title }: { children: ReactNode; title: string }) {
  const pathname = useRouterState({ select: (s) => s.location.pathname });
  const [open, setOpen] = useState(false);

  return (
    <div className="min-h-screen bg-[#f5f7fb] text-black">
      {/* Top bar */}
      <header className="sticky top-0 z-30 flex h-14 items-center justify-between gap-3 border-b bg-[#1F3864] px-4 text-white md:pl-64">
        <div className="flex min-w-0 items-center gap-3">
          <button
            className="grid h-9 w-9 shrink-0 place-items-center rounded-md hover:bg-white/10 md:hidden"
            onClick={() => setOpen(true)}
            aria-label="Abrir menú"
          >
            ☰
          </button>
          <h1 className="truncate text-base font-semibold sm:text-lg">{title}</h1>
        </div>
        <div className="hidden items-center gap-2 text-xs sm:flex">
          <span className="inline-block h-2 w-2 rounded-full bg-[#26A69A] shadow-[0_0_6px_#26A69A]" />
          16 modelos IA · IBKR
        </div>
      </header>

      {/* Desktop sidebar */}
      <aside className="fixed inset-y-0 left-0 z-20 hidden w-64 border-r bg-white md:block">
        <div className="flex h-14 items-center px-5 text-lg font-bold text-[#1F3864]">
          Invest<span className="text-[#C5961A]">AI</span>
        </div>
        <nav className="flex flex-col gap-1 px-3 pb-4">
          {NAV.map((n) => {
            const active = pathname === n.to;
            return (
              <Link
                key={n.to}
                to={n.to}
                className={`flex items-center gap-3 rounded-md px-3 py-2 text-sm font-medium transition ${
                  active
                    ? "bg-[#1F3864] text-white"
                    : "text-gray-700 hover:bg-[#f0f3f8] hover:text-[#1F3864]"
                }`}
              >
                <span className="text-base">{n.icon}</span> {n.label}
              </Link>
            );
          })}
        </nav>
        <div className="border-t px-5 py-3 text-[11px] text-gray-500">
          © 2025 InvestAI · v1.0
        </div>
      </aside>

      {/* Mobile drawer */}
      {open && (
        <div className="fixed inset-0 z-40 md:hidden" onClick={() => setOpen(false)}>
          <div className="absolute inset-0 bg-black/50" />
          <aside
            className="absolute inset-y-0 left-0 w-72 bg-white p-4 shadow-xl"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="mb-4 flex h-10 items-center justify-between">
              <span className="text-lg font-bold text-[#1F3864]">
                Invest<span className="text-[#C5961A]">AI</span>
              </span>
              <button onClick={() => setOpen(false)} aria-label="Cerrar">✕</button>
            </div>
            <nav className="flex flex-col gap-1">
              {NAV.map((n) => {
                const active = pathname === n.to;
                return (
                  <Link
                    key={n.to}
                    to={n.to}
                    onClick={() => setOpen(false)}
                    className={`flex items-center gap-3 rounded-md px-3 py-2.5 text-sm font-medium ${
                      active ? "bg-[#1F3864] text-white" : "text-gray-700 hover:bg-[#f0f3f8]"
                    }`}
                  >
                    <span>{n.icon}</span> {n.label}
                  </Link>
                );
              })}
            </nav>
          </aside>
        </div>
      )}

      {/* Content */}
      <main className="md:pl-64 pb-20 md:pb-0">{children}</main>

      {/* Mobile bottom nav (quick access) */}
      <nav className="fixed bottom-0 left-0 right-0 z-20 flex items-center justify-around border-t bg-white py-1.5 shadow-[0_-2px_8px_rgba(0,0,0,0.05)] md:hidden">
        {NAV.slice(0, 5).map((n) => {
          const active = pathname === n.to;
          return (
            <Link
              key={n.to}
              to={n.to}
              className={`flex flex-col items-center gap-0.5 px-3 py-1 text-[10px] font-medium ${
                active ? "text-[#1F3864]" : "text-gray-500"
              }`}
            >
              <span className="text-lg">{n.icon}</span> {n.label}
            </Link>
          );
        })}
      </nav>
    </div>
  );
}

export function ModuleFrame({ src }: { src: string }) {
  return (
    <div className="h-[calc(100vh-3.5rem)] w-full">
      <iframe
        src={src}
        title="módulo"
        className="h-full w-full border-0 bg-white"
      />
    </div>
  );
}