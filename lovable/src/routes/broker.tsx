import { createFileRoute } from "@tanstack/react-router";
import { AppShell, ModuleFrame } from "@/components/AppShell";

export const Route = createFileRoute("/broker")({
  head: () => ({
    meta: [
      { title: "Broker IBKR — InvestAI" },
      { name: "description", content: "Broker IBKR del sistema InvestAI." },
      { property: "og:title", content: "Broker IBKR — InvestAI" },
      { property: "og:description", content: "Broker IBKR del sistema InvestAI." },
    ],
  }),
  component: () => (
    <AppShell title="Broker IBKR">
      <ModuleFrame src="/modules/A8_broker.html" />
    </AppShell>
  ),
});
