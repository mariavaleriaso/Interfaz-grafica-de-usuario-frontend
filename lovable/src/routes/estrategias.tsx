import { createFileRoute } from "@tanstack/react-router";
import { AppShell, ModuleFrame } from "@/components/AppShell";

export const Route = createFileRoute("/estrategias")({
  head: () => ({
    meta: [
      { title: "Estrategias — InvestAI" },
      { name: "description", content: "Estrategias del sistema InvestAI." },
      { property: "og:title", content: "Estrategias — InvestAI" },
      { property: "og:description", content: "Estrategias del sistema InvestAI." },
    ],
  }),
  component: () => (
    <AppShell title="Estrategias">
      <ModuleFrame src="/modules/A6_estrategias.html" />
    </AppShell>
  ),
});
