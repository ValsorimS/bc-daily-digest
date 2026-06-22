---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central: understanding the Database Wait Statistics page."
published: true
original_date: 2026-01-28
---

Verdikt: ANO – Článek detailně rozebírá novou diagnostickou stránku "Database Wait Statistics" v Business Central, která je zásadní pro analýzu SQL bottlenecků přímo z prostředí BC.

<!--více-->

- Zavedení nové systémové stránky a virtuální tabulky "Database Wait Statistics" v BC, která zpřístupňuje nízkoúrovňové výkonové metriky SQL Serveru (wait stats) bez nutnosti přímého přístupu k databázové instanci.
- Možnost diagnostiky specifických typů čekání (např. transakční zámky LCK_M_*, diskové operace PAGEIOLATCH či CPU prostředky CXPACKET) pro přesnou identifikaci úzkých hrdel způsobených neefektivním AL kódem.
- Schopnost resetovat kumulované statistiky přímo z UI a korelovat naměřené hodnoty s telemetrickými signály v Azure Application Insights (KQL) pro pokročilý performance tuning a optimalizaci indexů.

[Číst celý článek](https://demiliani.com/2026/01/28/dynamics-365-business-central-understanding-the-database-wait-statistics-page/)