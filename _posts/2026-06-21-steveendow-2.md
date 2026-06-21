---
layout: post
title: "Steveendow: Exploring Business Central Custom Table Indexes"
published: true
original_date: 2022-05-20
---

Verdikt: NE – Článek pouze povrchně popisuje automatické vytváření klastrovaných SQL indexů u tabulkových rozšíření, což je pro zkušeného BC vývojáře dlouhodobě známý fakt.

<!--více-->

- SQL reprezentace tabulkových rozšíření (`tableextension`) využívá fyzické oddělené tabulky (companion tables), kde se na úrovni SQL Serveru automaticky generuje unikátní klastrovaný index (`Clustered Index`).
- Tento automatický index je definován striktně nad poli primárního klíče bazální tabulky (např. "No."), což je klíčové pro optimalizaci implicitních `JOIN` operací prováděných NST (Navision Service Tier).
- Text nepřináší žádné nové AL koncepty, informace o AI agentech ani moderní trendy, pouze vizuálně ověřuje standardní chování databázového schématu popsané v oficiální Microsoft dokumentaci.

[Číst celý článek](https://blog.steveendow.com/2022/05/exploring-business-central-custom-table.html)