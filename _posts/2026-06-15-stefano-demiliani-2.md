---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central: how many Copilot Credits my Agent consumes?"
published: true
original_date: 2026-03-24
---

Verdikt: ANO – Článek je zásadní pro architekty a vývojáře, kteří potřebují plánovat a optimalizovat náklady na provoz vlastních AI agentů integrovaných do Business Central.

<!--více-->

- Architektura licencování a spotřeby: Standardní agenti využívají sdílenou kapacitu Copilot v rámci BC licencí, zatímco vlastní AI agenti (vytvoření přes Copilot Studio nebo přímým AL voláním Azure OpenAI) konzumují specifické kredity (AI capacity units/tokens) v závislosti na počtu tokenů (vstup/výstup) a typu použitého LLM modelu.
- Telemetrie a monitoring: Pro přesné měření spotřeby vlastních AL integrací (při využití systémové komponenty `Copilot Capability` v AL) je nutné implementovat Azure Application Insights, kde lze analyzovat telemetrické signály, identifikovat neefektivní dotazy a sledovat přesný počet spotřebovaných tokenů.
- Optimalizace v AL kódu: Vývojář musí minimalizovat spotřebu kreditů optimalizací systémových promptů, omezením velikosti kontextového okna (předáváním pouze nezbytných JSON struktur místo celých datových sad z BC) a vhodným nastavením parametrů (např. token limitů a teploty) v AL objektu `Copilot Capability`.

[Číst celý článek](https://demiliani.com/2026/03/24/dynamics-365-business-central-how-many-copilot-credits-my-agent-consumes/)