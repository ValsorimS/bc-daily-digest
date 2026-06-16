---
layout: post
title: "Steveendow: Business Central Simple Tip #4: Exporting Leading Zeroes to Excel and then CSV- It works fine!"
published: true
original_date: 2023-01-19
---

Verdikt: NE – Článek řeší pouze triviální manuální workaround pro export dat z Business Central přes Excel do CSV se zachováním vedoucích nul a nepřináší žádné AL novinky, AI agenty ani moderní vývojářské trendy.

<!--více-->

- Návrh řešení využívá standardní akci "Open in Excel" nad custom List Page pro export platebních a fakturačních dat (remittance) namísto robustnější AL implementace přes XMLport, Query nebo Data Exchange Framework.
- Hlavním technickým rizikem při tomto postupu je nežádoucí chování MS Excel, který při interpretaci a následném uložení CSV souboru automaticky odstraňuje vedoucí nuly u textových polí (např. bankovní účty, kódy partnerů).
- Text postrádá jakýkoliv AL kód, konfiguraci, API integraci či novinky v platformě Business Central a zaměřuje se pouze na konceptuální validaci manuálního workflow uživatele.

[Číst celý článek](https://blog.steveendow.com/2023/01/business-central-simple-tip-4-exporting.html)