import { createFileRoute } from "@tanstack/react-router";
import { AppShell, ModuleFrame } from "@/components/AppShell";

export const Route = createFileRoute("/svm")({
  head: () => ({
    meta: [
      { title: "SVM Clasificación — InvestAI" },
      { name: "description", content: "SVM Clasificación del sistema InvestAI." },
      { property: "og:title", content: "SVM Clasificación — InvestAI" },
      { property: "og:description", content: "SVM Clasificación del sistema InvestAI." },
    ],
  }),
  component: () => (
    <AppShell title="SVM Clasificación">
      <ModuleFrame src="/modules/A3_svm.html" />
    </AppShell>
  ),
});
