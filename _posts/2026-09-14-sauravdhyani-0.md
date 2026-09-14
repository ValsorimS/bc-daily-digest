---
layout: post
title: "Sauravdhyani: Business Central 29.0: Major Change to Table Extensions and SQL Storage."
published: true
original_date: 2026-09-14
---

Verdikt: ANO – Zásadní článek ohlašující konec companion tabulek a přímou integraci polí z extenzí do SQL struktury bázové tabulky.

<!--více-->

- Konec companion model: V BC 29.0 jsou pole z `tableextension` fyzicky ukládána přímo do bázové SQL tabulky namísto dosavadního odděleného satelitního schématu.
- Eliminace JOINů: Odstranění implicitních `LEFT OUTER JOIN` dotazů na úrovni databázového enginu při čtení záznamů s extenzními poli přináší výrazné zrychlení I/O operací a čistší execution plány.
- Pokročilá indexace: Nový unifikovaný model umožňuje vytvářet nativní složené indexy kombinující standardní pole bázové tabulky s custom poli z extenze.

[Číst celý článek](https://www.sauravdhyani.com/2026/09/business-central-290-major-change-to.html)