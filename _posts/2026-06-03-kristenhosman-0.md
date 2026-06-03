---
layout: post
title: "kristenhosman: Master Data Management Setup in Microsoft Dynamics 365 Business Central"
published: true
original_date: 2026-03-17
---

Verdikt: NE – Článek popisuje pouze základní uživatelské nastavení standardní synchronizace kmenových dat (MDM) v klientském rozhraní bez jakéhokoliv přínosu pro AL vývoj, AI agenty nebo nové vývojářské trendy.

<!--více-->

- Nativní Master Data Management (MDM) umožňuje out-of-the-box replikaci tabulek G/L Account (T15), Dimension (T348) a Dimension Value (T349) ze zdrojové firmy (Source Company) do cílových entit bez psaní integračního AL kódu.
- Synchronizační engine využívá systémové nastavení v tabulkách "Master Data Management Setup" a "Synchronization Tables", kde se pro konkrétní ID tabulek aktivuje synchronizační pipeline změnou stavu na Enabled.
- Text neobsahuje žádné technické detaily pro AL vývojáře, jako je rozšíření synchronizační logiky přes eventy, řešení konfliktů v datech (coupling), AL API pro MDM nebo integrace s Copilotem.

[Číst celý článek](https://www.kristenhosman.com/2026/03/master-data-management-setup-in.html)