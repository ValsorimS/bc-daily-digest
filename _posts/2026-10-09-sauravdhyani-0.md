---
layout: post
title: "Sauravdhyani: Business Central 29: How Many Fields Can a Table Really Have?"
published: true
original_date: 2026-10-09
---

Verdikt: ANO – Přináší zásadní informaci o změně fyzického ukládání dat z table extension do SQL a s tím souvisejících limitech platformy v BC 29.

<!--více-->

- AL kompilátor v BC 29 nově emituje varování při přiblížení k SQL limitům pro počet normálních polí v tabulkách a jejich extenzích.
- Fyzické schéma mění architekturu: pole z `tableextension` se již neukládají do oddělených companion tabulek, ale přímo do bázové SQL tabulky.
- Eliminace SQL JOINů zlepšuje výkon čtení, ale kumulativně napříč všemi extenzemi naráží na tvrdé SQL Server limity (max. 1024 sloupců a 8060 bajtů na řádek).

[Číst celý článek](https://www.sauravdhyani.com/2026/09/business-central-29-how-many-fields-can.html)