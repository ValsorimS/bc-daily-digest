---
layout: post
title: "Sauravdhyani: Why No. Series Break After Upgrading to Business Central 27 (And How to Fix It)"
published: true
original_date: 2026-01-29
---

Verdikt: ANO – Článek je kritický pro vývojáře provádějící upgrade na Business Central v27, kteří se potýkají s neočekávaným selháním číslovacích řad (No. Series).

<!--více-->

- Kritická regrese v platformě Business Central v27 (SaaS i On-Prem) způsobující nefunkčnost generování a inkrementace číslovacích řad (No. Series) bezprostředně po upgradu prostředí.
- Problém je způsoben změnou v datové struktuře a systémové logice AL (přechod na nový model správy No. Series), což vede k selhání stávajícího AL kódu volajícího standardní inicializační procedury.
- Článek nabízí technický workaround a dočasný AL hotfix pro obnovení funkčnosti systému předtím, než Microsoft vydá oficiální platformovou opravu.

[Číst celý článek](https://www.sauravdhyani.com/2026/01/why-no-series-break-after-upgrading-to.html)