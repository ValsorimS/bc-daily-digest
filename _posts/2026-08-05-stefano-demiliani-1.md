---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central: AL transaction isolation levels and cache usage."
published: true
original_date: 2026-08-05
---

Verdikt: ANO – Článek přináší zásadní technické detaily o optimalizaci databázového výkonu a chování keše při použití metody Record.ReadIsolation v AL.

<!--více-->

- Metoda `Record.ReadIsolation` (od AL Runtime v11) umožňuje explicitně nastavovat izolační úroveň transakce pro konkrétní instanci záznamu před čtením.
- Podpora hodnot `ReadUncommitted`, `ReadCommitted`, `RepeatableRead` a `UpdLock` slouží k eliminaci SQL zamykání (lock contention) a přcházení deadlockům při vývoji.
- Zvolená izolační úroveň přímým způsobem určuje, zda dotaz obchází nebo využívá datovou keš NST (Middle-tier cache) a jak je garantována konzistence dat.

[Číst celý článek](https://demiliani.com/2026/08/05/dynamics-365-business-central-al-transaction-isolation-levels-and-cache-usage/)