---
layout: post
title: "Tech Sphere Dynamics: Business Central in the work conversation"
published: true
original_date: 2026-09-08
---

Verdikt: ANO – Zásadní čtení pro architekty a vývojáře AI integrací, které ukazuje implementaci moderního standardu Model Context Protocol (MCP) pro přímé napojení M365 Copilot na Business Central.

<!--více-->

- Nativní integrace Model Context Protocol (MCP) jako komunikační vrstvy mezi LLM (M365 Copilot) a Business Central, nahrazující těžkopádné custom pluginy standardizovaným protokolem pro volání nástrojů.
- Zabezpečení pomocí delegované identity (OAuth/Entra ID), kde agent dědí oprávnění konkrétního uživatele v BC, v kombinaci s dynamickým zjišťováním dostupných akcí (dynamic action discovery) mapovaných na vystavená API.
- Implementace striktního read-only rozsahu na úrovni rozhraní pro eliminaci rizika neautorizovaných zápisů přes LLM a dostupný step-by-step postup pro reprodukci konfigurace.

[Číst celý článek](https://techspheredynamics.com/2026/09/08/business-central-cowork-native-mcp/)