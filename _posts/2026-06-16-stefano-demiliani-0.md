---
layout: post
title: "Stefano Demiliani: Securely accessing an Azure OpenAI model from an Azure Logic Apps Standard AI agent using a Private Endpoint."
published: true
original_date: 2026-06-16
---

Verdikt: ANO – Článek popisuje kritický enterprise security pattern pro zabezpečení komunikace mezi AI agenty v Azure Logic Apps a Azure OpenAI pomocí privátních endpointů, což je klíčové pro bezpečné integrace s Business Central.

<!--více-->

- Architektura AI agentů postavených na Azure Logic Apps (Standard) vyžaduje pro bezpečné zpracování ERP dat z Business Central eliminaci veřejné síťové komunikace a striktní izolaci provozu.
- Technické řešení implementuje Azure Private Endpoints pro službu Azure OpenAI v kombinaci s VNet integrací na straně Logic Apps a správnou konfigurací privátních DNS zón (privatelink.openai.azure.com).
- Tento vzor umožňuje BC vývojářům bezpečně delegovat složité orchestrace AI agentů a RAG (Retrieval-Augmented Generation) scénáře mimo AL runtime, aniž by došlo k vystavení citlivých dat do veřejného internetu.

[Číst celý článek](https://demiliani.com/2026/06/16/securely-accessing-an-azure-openai-model-from-an-azure-logic-apps-standard-ai-agent-using-a-private-endpoint/)