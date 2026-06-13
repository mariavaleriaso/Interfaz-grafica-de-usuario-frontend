import { createFileRoute } from "@tanstack/react-router";
import { AppShell, ModuleFrame } from "@/components/AppShell";

export const Route = createFileRoute("/dashboard")({
  head: () => ({
    meta: [
      { title: "Dashboard Completo — InvestAI" },
      { name: "description", content: "Dashboard Completo del sistema InvestAI." },
      { property: "og:title", content: "Dashboard Completo — InvestAI" },
      { property: "og:description", content: "Dashboard Completo del sistema InvestAI." },
    ],
  }),
  component: () => (
    <AppShell title="Dashboard Completo">
      <ModuleFrame src="/modules/A9_dashboard.html" />
    </AppShell>
  ),
});
