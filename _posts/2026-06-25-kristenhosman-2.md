---
layout: post
title: "kristenhosman: RDLC how to make fields UPPERCASE in Dynamics 365 Business Central"
published: true
original_date: 2024-09-16
---

Verdikt: NE – Článek se zabývá základní úpravou RDL reportu bez souvislosti s AL, AI agenty či moderními trendy pro zkušené BC vývojáře.

<!--více-->

*   **Základní úprava RDL reportu:** Článek popisuje modifikaci RDL (Report Definition Language) layoutu reportu v Microsoft Report Builderu s cílem vynutit zobrazení textu velkými písmeny na šeku.
*   **RDL Expression Language:** Implementace využívá standardní RDL výraz `=UCase(Cstr(Choose(101,Split(Cstr(ReportItems!FooterInfo.Value), Chr(177)))))` aplikovaný na pole v reportu.
*   **String manipulace v RDL:** Technicky je demonstrováno použití funkce `UCase()` pro převod na velká písmena, `Cstr()` pro explicitní typovou konverzi na řetězec a kombinace `Split()` a `Choose()` pro (potenciálně komplexnější) extrakci podřetězce z hodnoty `ReportItems!FooterInfo.Value` přímo v RDL výrazu.

[Číst celý článek](https://www.kristenhosman.com/2024/09/rdlc-how-to-make-fields-uppercase-in.html)