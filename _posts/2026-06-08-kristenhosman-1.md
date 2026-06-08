---
layout: post
title: "kristenhosman: When Copy-Paste Goes Wrong: Fixing General Journal Field Order Issues in Business Central"
published: true
original_date: 2025-10-28
---

Verdikt: NE – Článek řeší pouze triviální chování sekvenční validace polí při vkládání dat z Excelu a nepřináší žádné nové AL funkce, AI agenty ani technologické trendy pro zkušené vývojáře.

<!--více-->

* Problém nežádoucího přepisování hodnoty v poli `Description` při hromadném vložení (Copy/Paste) dat z Excelu do řádků finančního deníku (General Journal).
* Sekvenční zpracování triggerů v klientské části: Business Central zpracovává a validuje vložená pole zleva doprava podle jejich fyzického pořadí v definici layoutu stránky (`Page`). Pokud je pole `Account No.` (a jeho `OnValidate` trigger) umístěno na stránce až za polem `Description`, dojde k přepsání uživatelského popisu výchozím názvem účtu z číselníku.
* Vývojářské řešení v AL: Pro správné fungování importů copy-paste je kritické v definici layoutu stránky (či v `pageextension`) striktně řadit řídicí pole (`Account Type`, `Account No.`) před pole závislá (`Description`), případně toto chování ošetřit aplikační logikou v příslušných event subscriberech.

[Číst celý článek](https://www.kristenhosman.com/2025/10/when-copy-paste-goes-wrong-fixing.html)