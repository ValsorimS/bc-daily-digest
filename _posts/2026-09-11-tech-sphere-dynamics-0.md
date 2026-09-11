---
layout: post
title: "Tech Sphere Dynamics: What an Agent Doesn’t Know It Doesn’t Know"
published: true
original_date: 2026-09-11
---

Verdikt: ANO – Nabízí zásadní architektonický vhled do limitů vlastního návrhu, modularity a rozhodování mezi over-engineeringem a standardními vzory platformy Business Central.

<!--více-->

- Architektonická dekompozice AL: Přechod od monolitického kódu k striktnímu oddělení odpovědností pomocí AL Interfaces, Namespace governance a striktního řízení scope (`Internal` vs. `Public`); definice hranice, kde custom logika ustupuje standardním extensibility bodům a hookům platformy.
- Role AI agentů a statické analýzy: Využití Copilot a specializovaných AI modelů pro generování boilerplate kódu a scaffoldingu integračních testů; delegování rutinní validace na pokročilý linter tooling (AppSourceCop, PerTenantExtensionCop, CodeCop), čímž se minimalizují limity lidského úsudku v syntaxi a best practices.
- SaaS-first paradigma a cloudové trendy: Opuštění snah o reimplementaci robustních backendových funkcí v čistém AL; přesun heavy-compute logiky a externích integrací do Azure Functions / Power Platform a zavedení monitoringu přes Application Insights pro reálná runtime data namísto subjektivního odhadu výkonu.

[Číst celý článek](https://techspheredynamics.com/2026/09/11/what-an-agent-doesnt-know-it-doesnt-know/)