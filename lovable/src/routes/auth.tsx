import { createFileRoute } from "@tanstack/react-router";
import { AppShell, ModuleFrame } from "@/components/AppShell";

export const Route = createFileRoute("/auth")({
  head: () => ({
    meta: [
      { title: "Autenticación — InvestAI" },
      { name: "description", content: "Autenticación del sistema InvestAI." },
      { property: "og:title", content: "Autenticación — InvestAI" },
      { property: "og:description", content: "Autenticación del sistema InvestAI." },
    ],
  }),
  component: () => (
    <AppShell title="Autenticación">
      <ModuleFrame src="/modules/A1_autenticacion.html" />
    </AppShell>
  ),
});
