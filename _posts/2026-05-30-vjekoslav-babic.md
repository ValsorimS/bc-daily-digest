---
layout: post
title: "Vjekoslav Babic: UBI won’t save us, and the nurse will tell you why"
published: true
---

# UBI won’t save us, and the nurse will tell you why

Zde je shrnutí zaměřené na technické dopady pro BC architekty a vývojáře:

* **Přechod na API-first AL architekturu pro AI agenty:** AI agenti vyžadují, aby BC fungoval jako bezhlavá platforma. Vývoj se přesouvá od UI k návrhu robustních API stránek, API dotazů a vázaných akcí (Bound Actions), které slouží jako standardizované nástroje (tool calling) pro LLM k autonomnímu spouštění business logiky.
* **Nativní AL AI integrace (Copilot Toolkit):** Moderní AL programování využívá jmenné prostory `System.AI` a objektové modely pro integraci Azure OpenAI. Klíčový je vývoj vlastních prompt dialogů, implementace RAG (Retrieval-Augmented Generation) přímo v AL a parsování nestrukturovaných AI výstupů do strukturovaných dat BC tabulek.
* **Nové nároky na bezpečnost a telemetrii:** S nástupem agentů se role vývojáře mění na kontrolora integrity. Je nutné implementovat striktní oprávnění (Permission Sets) specifická pro AI, robustní zpracování chyb (Try Functions zamezující zápisu nevalidních dat) a detailní monitorování AI operací přes Application Insights.

[Číst celý článek](https://vjeko.com/2026/05/30/ubi-wont-save-us-and-the-nurse-will-tell-you-why/)