import { createFileRoute } from "@tanstack/react-router";
import { AppShell, ModuleFrame } from "@/components/AppShell";

export const Route = createFileRoute("/mercado")({
  head: () => ({
    meta: [
      { title: "Datos de Mercado — InvestAI" },
      { name: "description", content: "Datos de Mercado del sistema InvestAI." },
      { property: "og:title", content: "Datos de Mercado — InvestAI" },
      { property: "og:description", content: "Datos de Mercado del sistema InvestAI." },
    ],
  }),
  component: () => (
    <AppShell title="Datos de Mercado">
      <ModuleFrame src="/modules/A2_mercado.html" />
    </AppShell>
  ),
});
