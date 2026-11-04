---
layout: post
title: "Stefano Demiliani: Giving an AI agent the keys to Business Central: practical security tips."
published: true
original_date: 2026-11-04
---

Verdikt: NE – úryvek pouze nastiňuje budoucí scénář interakce AI agentů s Business Centralem, neobsahuje technické detaily k AL, konkrétním AI integracím nebo novým vývojovým prvkům.

<!--více-->

*   **AI jako externí integrace:** Koncept autonomního AI agenta zpracovávajícího faktury naznačuje intenzivní **integraci Business Centralu s externími AI službami**. To vyžaduje **robustní a performantní AL API vrstvu (OData/Custom API Pages)** pro čtení (dodavatelská data, existující faktury) a zápis (nové nákupní faktury, přílohy), s důrazem na minimalizaci transakčních latencí.
*   **Důraz na zabezpečení přístupu:** Z kontextu odkazu (security tips) vyplývá, že klíčovým aspektem pro implementaci takových AI agentů je **granularní řízení přístupu a autorizace**. Zkušený AL vývojář musí navrhovat a implementovat **přesné sady oprávnění (Permission Sets)** a využívat **moderní autentizační mechanismy (OAuth 2.0 / Azure AD app registration)** pro externí služby.
*   **Strategický posun k bezhlavému (headless) BC:** Scénář předpovídá trend, kdy BC funguje jako jádro dat a procesů, se stále větší automatizací řízenou externími agenty. Pro AL vývojáře to znamená zvýšenou potřebu vytvářet **rozšiřitelné moduly s dobře definovanými eventy a rozhraními** pro integraci, namísto zaměření čistě na uživatelské rozhraní. Datace 2026 naznačuje budoucí směřování.

[Číst celý článek](https://demiliani.com/2026/11/04/giving-an-ai-agent-the-keys-to-business-central-practical-security-tips/)