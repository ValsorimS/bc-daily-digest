---
layout: post
title: "VS Code Blog: Beyond the tools, adding MCP in VS Code"
published: true
original_date: 2025-05-14
---

Verdikt: ANO – Článek popisuje integraci Model Context Protocol (MCP) do VS Code agent modu, což AL vývojářům otevírá cestu k tvorbě vlastních AI kopilotů pro automatizaci vývoje a údržby Business Central aplikací.

<!--více-->

- Podpora MCP (Model Context Protocol) ve VS Code Copilot Agent Mode umožňuje LLM autonomně volat lokální i vzdálené nástroje přes standardizované JSON-RPC 2.0 rozhraní přímo v kontextu IDE.
- Pro AL vývojáře to znamená možnost vytvořit vlastní MCP servery (např. v Node.js/Pythonu) a zpřístupnit AI agentovi AL compiler (alc.exe), AL parser, volání Business Central API, správu Docker kontejnerů přes PowerShell nebo analýzu telemetrie.
- AI agent dokáže v tomto režimu samostatně řešit komplexní tasky, jako je refaktorizace kódu podle BC standardů, generování integračních API stránek, oprava chyb na základě výstupu z kompilátoru nebo automatické psaní AL testů s využitím lokálních nástrojů.

[Číst celý článek](https://code.visualstudio.com/blogs/2025/05/12/agent-mode-meets-mcp)