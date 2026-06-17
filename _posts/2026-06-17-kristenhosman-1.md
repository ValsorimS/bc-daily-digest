---
layout: post
title: "kristenhosman: Automating Deferred Revenue in Business Central Using Recurring Sales Lines"
published: true
original_date: 2025-07-26
---

Verdikt: NE – Článek popisuje základní, dlouhodobě dostupnou standardní funkcionalitu pro automatické odložení výnosů v BC, neobsahuje žádné technické novinky pro AL vývojáře, ani zmínky o AI či aktuálních trendech.

<!--více-->

*   `Default Deferral Template` na kartě `G/L Account` (pole `Default Deferral Template` v tabulce 15 `G/L Account`) automaticky přiřazuje kód odložení výnosů (`Deferral Code`) při použití daného účtu na řádku prodeje.
*   Integrace se `Recurring Sales Lines` (tabulka 326 `Recurring Sales Line`): Systém automaticky přebírá `Deferral Code` z definovaného `Default Deferral Template` na G/L účtu do generovaných `Sales Lines` (tabulka 37 `Sales Line`).
*   Automatizace procesu odložení výnosů: Při zaúčtování `Sales Invoice` (tabulka 112 `Sales Invoice Header` a 113 `Sales Invoice Line`) dochází k automatickému vytvoření a zaúčtování položek odložení výnosů (`Deferral Entries`) dle definovaného template.

[Číst celý článek](https://www.kristenhosman.com/2025/07/automating-deferred-revenue-in-business.html)