---
layout: post
title: "Steveendow: The Two Big Mistakes Made In Business Central Number Series, IMHO"
published: true
original_date: 2025-10-15
---

Verdikt: NE – Text neobsahuje žádné technické novinky v AL, AI agenty ani technologické trendy, ale pouze kritizuje elementární chyby konzultantů při konfiguraci číselných řad (No. Series).

<!--více-->

- Kritika nekritického kopírování výchozí konfigurace číselných řad z demo databáze Cronus do produkčních prostředí, což vede k okamžitým konfliktům při ostrém provozu.
- Riziko selhání transakcí při účtování (Posting) v důsledku špatně nastavených limitů "Ending No." v tabulce "No. Series Line", což způsobuje runtime chyby zamezující zápisu do věcné knihy.
- Z pohledu AL vývoje a architektury je nutné při návrhu customizací správně implementovat modul "No. Series" ze System Application a ošetřit mezní stavy (např. vyčerpání řady) tak, aby uživatelé nenaráželi na fatální chyby uprostřed transakčních bloků.

[Číst celý článek](https://blog.steveendow.com/2025/10/the-two-big-mistakes-made-in-business.html)