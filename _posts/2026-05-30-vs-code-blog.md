---
layout: post
title: "VS Code Blog: Visual Studio Code 1.123"
published: true
---

# Visual Studio Code 1.123

Zde je technické shrnutí novinek ve VS Code 1.123 (Insiders) s dopadem na AL a Business Central development:

*   **Hlubší integrace AI Agentů (GitHub Copilot):** Verze 1.123 posiluje "agentické" programování pomocí pokročilého kontextového vnímání workspace (`@workspace`). BC vývojáři mohou pomocí AI agentů generovat komplexní AL boilerplate (např. API stránky, query objekty) a automatizovat refaktoring legacy C/AL kódu s plným vědomím závislostí v `app.json`.
*   **Optimalizace AL Language Extension přes nová API:** Nová interní API rozhraní editoru umožňují Microsoftu lépe integrovat AL kompilátor a analyzéry s AI. To se projeví v přesnějším inline doplňování kódu (IntelliSense poháněné AI) a schopnosti AI navrhovat opravy přímo pro specifické BC varování a chyby (CodeActions).
*   **Zefektivnění Multi-project Workspaces a CLI:** Vylepšená správa terminálů a multi-file operací usnadňuje orchestraci AL-Go pro GitHub pipelines a práci v monorepo projektech. To zrychluje testování přes local BC kontejnery a nasazování více provázaných AL aplikací současně.

[Číst celý článek](https://code.visualstudio.com/updates/v1_123)