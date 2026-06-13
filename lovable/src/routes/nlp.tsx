import { createFileRoute } from "@tanstack/react-router";
import { AppShell, ModuleFrame } from "@/components/AppShell";

export const Route = createFileRoute("/nlp")({
  head: () => ({
    meta: [
      { title: "NLP Sentimiento — InvestAI" },
      { name: "description", content: "NLP Sentimiento del sistema InvestAI." },
      { property: "og:title", content: "NLP Sentimiento — InvestAI" },
      { property: "og:description", content: "NLP Sentimiento del sistema InvestAI." },
    ],
  }),
  component: () => (
    <AppShell title="NLP Sentimiento">
      <ModuleFrame src="/modules/A5_nlp.html" />
    </AppShell>
  ),
});
