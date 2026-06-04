---
layout: post
title: "Vjekoslav Babic: The MCP Bridge: AL Language Tools for Every Agent"
published: true
original_date: 2026-05-03
---

Verdikt: NE – Text pouze povrchně načrtává frustraci z nefunkčnosti obecných AI nástrojů v AL a končí dříve, než nabídne jakékoliv technické řešení nebo hlubší analýzu.

<!--více-->

* Obecné AI nástroje a editory (Cursor, Claude Code, GitHub Copilot) naráží v AL na absenci nativního parseru, neznalost specifické syntaxe a neschopnost pracovat s proprietárním systémem symbolů a referencí z `.app` balíčků.
* Trendem pro integraci AI do AL vývoje je tvorba vlastních MCP (Model Context Protocol) serverů nebo lokálních RAG pipeline, které AI agentům zpřístupňují definice standardních BC tabulek, custom objektů a aplikační logiky Base Application.
* Pro efektivní generování validního AL kódu pomocí AI agentů je nezbytné implementovat automatické smyčky zpětné vazby (feedback loops) využívající AL compiler (`alc.exe`) pro validaci syntaktické správnosti a dodržování BC design patterns (např. Handled Pattern, Singleton).

[Číst celý článek](https://vjeko.com/2026/05/03/the-mcp-bridge-al-language-tools-for-every-agent/)