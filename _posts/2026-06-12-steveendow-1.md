---
layout: post
title: "Steveendow: Filter by Date Range with Business Central Web API v2.0 - OData date filter syntax"
published: true
original_date: 2024-02-23
---

Verdikt: NE – Článek neobsahuje technické novinky týkající se AL, AI agentů nebo obecných trendů v MS Dynamics 365 Business Central, zaměřuje se na konkrétní syntaktický problém OData API.

<!--více-->

*   Business Central Web API v2.0 OData endpointy, konkrétně `generalLedgerEntries`, mohou při dotazu bez filtru vracet nadměrné objemy dat, což vede k chybám 'response too large'.
*   Standardní OData syntax pro filtrování datumu s `datetime'YYYY-MM-DDTHH:MM:SS.mmm'` (např. `postingDate ge datetime'2022-01-01T00:00:00.000'`) není kompatibilní s BC Web API v2.0.
*   Korektní formát pro filtrování datových polí v Business Central Web API v2.0 OData dotazech vyžaduje prostý formát `YYYY-MM-DD` (např. `generalLedgerEntries/?$filter=postingDate ge 2021-01-01 and postingDate le 2022-12-31`).

[Číst celý článek](https://blog.steveendow.com/2024/02/filter-by-date-range-with-business.html)