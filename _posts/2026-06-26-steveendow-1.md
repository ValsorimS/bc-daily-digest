---
layout: post
title: "Steveendow: Business Central Web API Error When Using $expand"
published: true
original_date: 2022-03-05
---

Verdikt: NE – Krátký příspěvek se zabývá pouze nefunkční OData syntaxí wildcard expandu v API Business Central, která při testování končí chybou.

<!--více-->

- Pokus o využití OData query parametru `$expand=*` pro automatické rozvinutí všech navigačních vlastností (Navigation Properties) v rámci Web API endpointů Business Central.
- Praktické testování této zástupné syntaxe (wildcard) v Postmanu selhává na chybové zprávě platformy, což značí nekompatibilitu s OData engine v BC.
- Pro integrace a AL vývoj je tato metoda nepoužitelná a z hlediska výkonu nevhodná; je nutné nadále explicitně definovat konkrétní rozšiřované datové struktury.

[Číst celý článek](https://blog.steveendow.com/2022/03/business-central-web-api-error-when.html)