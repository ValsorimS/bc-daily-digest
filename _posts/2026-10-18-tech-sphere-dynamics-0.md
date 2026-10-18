---
layout: post
title: "Tech Sphere Dynamics: Your AI agent writes AL. Can it explain why it fails?"
published: true
original_date: 2026-10-18
---

Verdikt: ANO – Přináší zásadní vhled do automatizace AL snapshot debuggingu pomocí AI agentů, což přímo ovlivňuje diagnostiku a profilování kódu v runtime.

<!--více-->

- **Autonomní snapshot debugging:** Přechod od manuální inicializace snapshotu přes `launch.json` k událostmi řízenému záchytu, kdy AI agent autonomně aktivuje profiling na základě telemetrie chyb nebo anomálií v exekučním čase.
- **Integrace diagnostických nástrojů:** Využití kombinace Business Central Telemetry (Application Insights / KQL), platformních debugging API a AL Language serveru pro extrakci AST, call stacku a paměťových stavů proměnných.
- **Verifikace výstupu a integrita dat:** AI diagnostiku je nutné validovat vůči raw datům z `.alpackages` a execution trace; kritická je kontrola halucinací při interpretaci DB locků, flowfields kalkulací a sanitizace PII dat v zachycených datasetech.

[Číst celý článek](https://techspheredynamics.com/2026/10/18/business-central-v29-ai-agent-snapshot-debugging-evidence/)