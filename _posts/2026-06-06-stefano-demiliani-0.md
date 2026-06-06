---
layout: post
title: "Stefano Demiliani: Business Central Cloud Migration: be careful on reusing the same self-hosted runtime."
published: true
original_date: 2026-04-24
---

Verdikt: ANO – Článek detailně rozebírá skrytá rizika a selhání replikace dat při pokusu o sdílení jedné instance Self-hosted Integration Runtime (SHIR) mezi více cílovými prostředími Dynamics 365 Business Central.

<!--více-->

* Při migraci dat z on-premises do cloudu pomocí Cloud Migration toolu vede bezhlavé opětovné použití identické instalace Self-hosted Integration Runtime (SHIR) pro různé cílové tenanty nebo prostředí k okamžité invalidaci integračních tokenů a selhání běžících pipeline.
* Architektura na pozadí využívá Azure Data Factory (ADF), kde registrace stávající gateway pod novým autentizačním klíčem (např. při testování migrace do sandboxu a následně do produkce) tichým způsobem deautorizuje předchozí aktivní spojení, což zapříčiní chyby konektivity bez jasného varování v BC Admin Centru.
* Pro bezpečný deployment se striktně vyžaduje provisionovat dedikovaný SHIR pro každé cílové prostředí (environment isolation), nebo při nutnosti re-use provést kompletní odinstalaci lokálního integračního hostitele, promazání ADF metadat a novou čistou registraci s novým klíčem.

[Číst celý článek](https://demiliani.com/2026/04/24/business-central-cloud-migration-be-careful-on-reusing-the-same-self-hosted-runtime/)