---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central (and friends): where does your Copilot prompt go?"
published: true
original_date: 2026-09-22
---

Verdikt: ANO – Článek poskytuje zásadní architektonický vhled do problematiky směrování promptů a data residency mezi Business Central Online a Azure OpenAI (AOAI).

<!--více-->

- Globální dostupnost Copilot a Agent runtime v BC Online neznamená automaticky lokální instanci AOAI; dochází k decoupling aplikační vrstvy tenantu od výpočetní kapacity velkých jazykových modelů (LLM).
- Architektura směrování promptů využívá cross-geo data transit: pokud není AOAI dostupná v geografické zóně daného tenantu, požadavky jsou orchestrátorem směrovány do jiných datacenter na základě explicitního governance souhlasu administrátora.
- Implikace pro vývoj v AL: Při návrhu vlastních AI agentů a implementaci pomocí Copilot Toolkitu (např. přes page type `PromptDialog`) je nutné počítat se zvýšenou latencí cross-region volání a architektonickými omezeními compliance (GDPR, EU Data Boundary).

[Číst celý článek](https://demiliani.com/2026/09/22/dynamics-365-business-central-and-friends-where-does-your-copilot-prompt-go/)