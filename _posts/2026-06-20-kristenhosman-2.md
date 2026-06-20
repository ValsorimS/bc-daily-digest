---
layout: post
title: "kristenhosman: Over-Receipt Code for Purchase Orders"
published: true
original_date: 2025-04-29
---

Verdikt: NE – Článek popisuje pouze základní funkční nastavení standardní tolerance příjmu v klientském rozhraní a nepřináší žádné AL, vývojové ani AI novinky.

<!--více-->

- Standardní funkčnost Over-Receipt umožňuje příjem zboží nad objednané množství na základě procentuální tolerance definované v tabulce `Over-Receipt Code` (ID 5850).
- Datové vazby jsou řízeny přímo na kartě položky (`Item`, tabulka 27) nebo u prodejce, přičemž systém při zápisu do nákupního řádku validuje pole `Qty. to Receive` a automaticky plní `Over-Receipt Quantity`.
- Součástí je integrace na schvalovací workflow (příznak `Approval Required`), která aktivuje standardní schvalovací procesy pro nákupní příjemky před jejich zaúčtováním bez nutnosti psaní custom AL kódu.

[Číst celý článek](https://www.kristenhosman.com/2025/04/over-receipt-code-for-purchase-orders.html)