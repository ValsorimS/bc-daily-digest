---
layout: post
title: "kristenhosman: Deleting companies in Dynamics 365 Business Central v 24.3"
published: true
original_date: 2024-08-23
---

Verdikt: NE – Text popisuje pouze triviální uživatelský postup pro smazání firmy v klientském rozhraní a nepřináší žádné technické informace pro AL vývojáře, architekty ani zmínky o AI.

<!--více-->

- Článek se omezuje na základní UI proceduru odstranění firmy přes systémovou stránku „Companies“ (ID 357) ve verzi v24.3.
- Zmíněná operace spouští standardní kaskádové mazání dat (provádí trigger `OnDelete` na tabulce Company), přičemž jedinou možností obnovy je Point-in-Time Restore (PITR) celého prostředí přes Admin Center.
- Text zcela postrádá jakýkoliv vývojářský kontext, jako je správa databází pomocí AL kódu, automatizace přes Admin Center API, Tenant Management, nebo integrace s Copilotem.

[Číst celý článek](https://www.kristenhosman.com/2024/08/deleting-companies-in-dynamics-365.html)