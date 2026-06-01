---
layout: post
title: "VS Code Blog: Visual Studio Code 1.122"
published: true
original_date: 2026-05-28
---

1. **Verdikt: ANO.** Pro AL vývojáře je nezbytné sledovat aktualizace VS Code, protože přímo ovlivňují výkon AL Language extension, efektivitu GitHub Copilot (AI) při psaní kódu a stabilitu ladění (debuggingu) Business Central sandboxů.

<!--více-->

2. **Technické shrnutí:**
* **Pokročilá integrace AI agentů (GitHub Copilot):** Nová verze přináší hlubší kontextové porozumění pro AI agenty v chatu a inline režimu, což výrazně urychluje generování AL boilerplate kódu (např. definice tabulek, stránek a permission setů) a usnadňuje refaktorizaci legacy kódu.
* **Optimalizace Language Server Protocol (LSP) a workspace:** Vylepšení správy paměti a rychlosti LSP přímo zrychluje odezvu AL kompilátoru na pozadí, indexaci symbolů (zejména při načítání rozsáhlých bff/app souborů Base Application) a stabilizuje práci v multi-root workspaces.
* **Vylepšené ladění a správa zdrojového kódu:** Aktualizované rozhraní pro správu Git konfliktů (3-way merge) a vylepšené API pro debugovací protokoly (DAP) umožňují plynulejší trasování AL kódu, efektivnější analýzu call stacku při runtime chybách a spolehlivější hot-reload (Ctrl+F5) do BC prostředí.

[Číst celý článek](https://code.visualstudio.com/updates/v1_122)