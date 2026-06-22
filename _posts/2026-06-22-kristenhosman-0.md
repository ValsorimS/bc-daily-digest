---
layout: post
title: "kristenhosman: Reversing a posted journal entry in Dynamics 365 Business Central"
published: true
original_date: 2024-11-20
---

Verdikt: NE – Článek popisuje pouze elementární uživatelský postup pro stornování věcných položek bez jakékoliv technické přidané hodnoty nebo novinek pro AL vývojáře.

<!--více-->

- Standardní proces reverzace transakcí je iniciován ze stránky `G/L Entries` (ID 20) voláním systémové logiky pro storno, která generuje protizápisy do věcné knihy.
- Aplikační datová validace před spuštěním transakce ověřuje constraints typu povolené datum účtování (`User Setup` / `General Ledger Setup`) a stav uzavřeného účetního nebo daňového období.
- Článek zcela postrádá jakýkoliv AL kód, integrační eventy (např. v `Codeunit 12`), AI agenty (Copilot) či moderní technologické trendy platformy Business Central.

[Číst celý článek](https://www.kristenhosman.com/2024/11/reversing-posted-journal-entry-in.html)