---
layout: post
title: "kristenhosman: Running the Expense Agent in Microsoft Dynamics 365 Business Central (Version 28.1)"
published: true
original_date: 2026-06-28
---

Verdikt: NE – Text je pouze stručným uživatelským manuálem pro workflow schvalování účtenek a neobsahuje žádný AL kód, API specifikace ani hlubší architektonické detaily implementace AI agenta.

<!--více-->

- Představení autonomního AI „Expense Agenta“ pro Business Central (kontextově cíleno na budoucí v.28.1), který asynchronně zpracovává příchozí e-mailové PDF přílohy a transformuje nestrukturovaná data na strukturované BC entity bez nutnosti klasických externích OCR služeb.
- Architektura využívá design pattern „human-in-the-loop“, kde LLM agent provede ingest a extrakci dat pro vytvoření draftu nákladového dokladu, ale finální validaci a spuštění schvalovacího workflow (Approval Workflow) ponechává na uživateli.
- Z pohledu AL vývoje se jedná o integraci e-mailového subsystému s novým agentickým Copilot frameworkem, což potvrzuje trend nahrazování hardcoded integračních můstků flexibilnějšími LLM-based agenty přímo v jádru ERP.

[Číst celý článek](https://www.kristenhosman.com/2026/06/running-expense-agent-in-microsoft.html)