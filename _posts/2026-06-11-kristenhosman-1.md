---
layout: post
title: "kristenhosman: Crediting Invoices for a Customer That Are Associated with a Purchase Order Drop Shipment"
published: true
original_date: 2025-09-18
---

Verdikt: NE – Text popisuje pouze základní uživatelské postupy pro obcházení funkčního omezení u drop shipmentu a neobsahuje žádný AL kód, vývojářské novinky ani témata týkající se AI.

<!--více-->

- Systémové omezení Business Central blokuje standardní akce opravy a stornování (Correct/Cancel) na zaúčtovaných prodejních fakturách, pokud jsou řádky propojeny s nákupní objednávkou přes Drop Shipment.
- Pro opravu chyb v cenotvorbě je nutné manuálně generovat prodejní dobropis (Sales Credit Memo) na rozdíl částky a provést aplikaci na původní fakturu, případně provést úplné manuální storno a novou fakturaci včetně korekce DPH.
- Proces vratek u Drop Shipmentu vyžaduje provázané workflow, kde se z prodejní vratky (Sales Return Order) generuje nákupní vratka (Purchase Return Order) pomocí standardní funkce pro tvorbu souvisejících dokladů (Create Return-Related Documents).

[Číst celý článek](https://www.kristenhosman.com/2025/09/crediting-invoices-for-customer-that.html)