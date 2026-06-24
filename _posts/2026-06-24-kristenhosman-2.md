---
layout: post
title: "kristenhosman: Remittance Advice modification in Dynamics 365 Business Central"
published: true
original_date: 2024-09-16
---

Verdikt: NE – Článek popisuje pouze triviální úpravu RDLC layoutu v Report Builderu a nepřináší žádné nové informace pro AL vývoj, AI agenty ani moderní Business Central trendy.

<!--více-->

- Maskování citlivých bankovních údajů (Transit No., Bank Account No.) na standardním reportu 10083 (Remittance Advice) z důvodu bezpečnosti při e-mailové distribuci.
- Úprava hodnoty v RDLC layoutu pomocí vestavěného výrazu (Expression) v Report Builderu: `="***"+Right(Cstr(Choose(4,Split(Cstr(ReportItems!values.Value),Chr(177)))),4)`, který parsuje řetězec oddělený znakem s ASCII kódem 177 a extrahuje poslední 4 znaky.
- Nasazení probíhá standardní cestou bez nutnosti psaní AL kódu (stažení custom layoutu, editace v Microsoft Report Builderu, re-import a nastavení jako výchozí v Report Layout Selections).

[Číst celý článek](https://www.kristenhosman.com/2024/09/remittance-advice-modification-in.html)