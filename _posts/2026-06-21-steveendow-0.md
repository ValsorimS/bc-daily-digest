---
layout: post
title: "Steveendow: Disable The Annoying Dialog After Posting in Business Central"
published: true
original_date: 2022-07-28
---

Verdikt: NE – Článek popisuje pouze základní postup analýzy BaseApp kódu pro potlačení standardního dialogu po zaúčtování dokladu, což pro zkušeného AL vývojáře nepředstavuje žádnou novou informaci ani technologický trend.

<!--více-->

- Analýza možností potlačení standardního potvrzovacího dialogu nabízejícího otevření zaúčtovaného dokladu (např. nákupní faktury) bezprostředně po dokončení posting rutiny.
- Využití lokálního repozitáře BC Code History pro reverzní inženýrství a trasování kódu přímo v BaseApp (konkrétně v `PurchaseInvoice.Page.al`).
- Snaha o eliminaci dialogu pomocí Per-Tenant Extension (PTE) skrze event subscribery potlačující UI interakce (případně přes `Instruction Mgt.` / Notification Management).

[Číst celý článek](https://blog.steveendow.com/2022/07/disable-annoying-dialog-after-posting.html)