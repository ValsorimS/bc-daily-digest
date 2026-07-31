---
layout: post
title: "Steveendow: Reducing the Risk of Business Central Web API Secrets Through Education"
published: true
original_date: 2026-07-31
---

Verdikt: NE – Článek neobsahuje žádné technické novinky o AL ani AI agentech, jde pouze o odstrašující případ chybné konfigurace OAuth a hrubého porušení bezpečnosti integrátorem.

<!--více-->

- Absence technických novinek: Text nepřináší žádné nové AL APIs, funkce platformy BC ani AI agenty, zaměřuje se výhradně na selhání lidského faktoru při API integraci.
- OAuth 2.0 a zastaralá autentizace: Incident popisuje pokusy o připojení k BC Web API (ODataV4) pomocí zastaralých Web Access Keys (vyřazeny v roce 2022) a neschopnost správně nakonfigurovat OAuth 2.0 grant flow v aplikaci Postman.
- Bezpečnostní detaily integrace: Popisuje záměnu hodnot Client ID a Client Secret v hlavičkách požadavků, ukládání tajných klíčů v nešifrovaném plain-textu a únik kredenciálů přes veřejně přístupný videozáznam.

[Číst celý článek](https://blog.steveendow.com/2026/07/reducing-risk-of-business-central-web.html)