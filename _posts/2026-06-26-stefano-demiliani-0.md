---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central: Using Semantic Search from AL"
published: true
original_date: 2026-06-26
---

Verdikt: ANO – Článek ukazuje, jak přímo v AL implementovat sémantické vyhledávání pomocí embeddingů, což je klíčové pro integraci pokročilých AI agentů a RAG scénářů v Business Central.

<!--více-->

- Integrace sémantického vyhledávání do Business Central s využitím AL kódu pro generování vektorových embeddingů z ERP dat pomocí Azure OpenAI API.
- Architektura Retrieval-Augmented Generation (RAG) v AL, která umožňuje dynamicky vyhledávat relevantní nestrukturovaná data a předávat je jako kontext pro LLM/Copilota.
- Technická realizace postavená na odesílání JSON payloadů s textovými daty přes `HttpClient` na embedding modely a následné vektorové porovnávání nad externí databází.

[Číst celý článek](https://demiliani.com/2026/06/26/dynamics-365-business-central-using-semantic-search-from-al/)