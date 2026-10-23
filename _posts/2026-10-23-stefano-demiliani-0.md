---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central: introducing the new “Recent Record” virtual table"
published: true
original_date: 2026-10-23
---

Verdikt: ANO – Článek odhaluje novou interní virtuální tabulku pro sledování historie záznamů, což je klíčový stavební kámen pro kontextuální AI agenty a pokročilé AL patterny.

<!--více-->

- BC v29 zavádí novou virtuální tabulku `Recent Record`, která na úrovni platformy automaticky zachycuje naposledy navštívené a otevřené záznamy uživatele v reálném čase bez nutnosti psát custom telemetrii.
- V AL tabulka poskytuje přímý přístup k metadatům jako `Table ID`, `Record ID` (či Bookmark), `User Security ID` a timestampu, což umožňuje okamžité načtení dat přes `RecordRef` bez zátěže transakční SQL databáze.
- Primární architektonické využití spočívá v groundingu AI agentů (poskytnutí bezprostředního kontextu práce uživatele pro LLM prompty) a v nativní implementaci MRU (Most Recently Used) seznamů přímo v business logice.

[Číst celý článek](https://demiliani.com/2026/10/23/dynamics-365-business-central-introducing-the-new-recent-record-virtual-table/)