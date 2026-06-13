import { createFileRoute } from "@tanstack/react-router";
import { AppShell, ModuleFrame } from "@/components/AppShell";

export const Route = createFileRoute("/portafolio")({
  head: () => ({
    meta: [
      { title: "Portafolio — InvestAI" },
      { name: "description", content: "Portafolio del sistema InvestAI." },
      { property: "og:title", content: "Portafolio — InvestAI" },
      { property: "og:description", content: "Portafolio del sistema InvestAI." },
    ],
  }),
  component: () => (
    <AppShell title="Portafolio">
      <ModuleFrame src="/modules/A7_portafolio.html" />
    </AppShell>
  ),
});
