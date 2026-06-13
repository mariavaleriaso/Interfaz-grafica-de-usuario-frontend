import { createFileRoute } from "@tanstack/react-router";
import { AppShell, ModuleFrame } from "@/components/AppShell";

export const Route = createFileRoute("/lstm")({
  head: () => ({
    meta: [
      { title: "LSTM Pronóstico — InvestAI" },
      { name: "description", content: "LSTM Pronóstico del sistema InvestAI." },
      { property: "og:title", content: "LSTM Pronóstico — InvestAI" },
      { property: "og:description", content: "LSTM Pronóstico del sistema InvestAI." },
    ],
  }),
  component: () => (
    <AppShell title="LSTM Pronóstico">
      <ModuleFrame src="/modules/A4_lstm.html" />
    </AppShell>
  ),
});
