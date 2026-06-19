---
layout: post
title: "VS Code Blog: What 50,000 Runs of a 5-Line Eval Taught Us"
published: true
original_date: 2026-06-19
---

Verdikt: ANO – Článek odkrývá kritická data z 50 000 exekucí kódovacích LLM přímo v prostředí VS Code, což je klíčové pro efektivní integraci AI agentů a optimalizaci tokenových nákladů při vývoji v AL.

<!--více-->

* Analýza chování LLM při reálném vývoji ve VS Code ukazuje, jak modely dynamicky škálují výpočetní úsilí (effort), spotřebu tokenů a volání nástrojů (tool use) i u banálních syntaktických úprav, což přímo ovlivňuje návrh AL Copilot agentů.
* Data poskytují vodítko pro optimální selekci modelů (např. volbu mezi reasoning modely a menšími rychlými modely) pro specifické AL úlohy, jako je generování boilerplate kódu, AL test suite nebo refaktorování tabulkových extenzí.
* Pochopení korelace mezi složitostí promptu, kontextovým oknem a reálným využitím VS Code API (tool calling) umožňuje AL vývojářům lépe designovat vlastní custom agenty a minimalizovat finanční náklady na tokeny při automatické migraci kódu.

[Číst celý článek](https://code.visualstudio.com/blogs/2026/06/19/what-50000-runs-taught-us)