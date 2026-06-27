---
layout: post
title: "Stefano Demiliani: Securing your Azure Storage Account: a guide to enabling Business Central-only access using Network Security Perimeter."
published: true
original_date: 2025-12-22
---

Verdikt: ANO – Článek řeší kritické zabezpečení Azure Storage pro BC SaaS pomocí Network Security Perimeter (NSP), což eliminuje bezpečnostní rizika veřejných endpointů a je klíčové pro enterprise integrace.

<!--více-->

- Implementace Network Security Perimeter (NSP) pro Azure Storage, která izoluje datové úložiště a povoluje příchozí komunikaci striktně pouze z definovaných Business Central SaaS prostředí.
- Odstranění nutnosti whitelistování nestabilních a dynamických odchozích IP adres BC platformy; komunikace je zabezpečena na transportní vrstvě Azure bez vystavení storage do veřejného internetu.
- Architektonický posun AL integrací (využívajících `HttpClient` nebo Azure Storage Services knihovny) směrem k zero-trust síťové bezpečnosti, kde identita volajícího BC tenanta odpovídá síťovému perimetru Azure prostředku.

[Číst celý článek](https://demiliani.com/2025/12/22/securing-your-azure-storage-account-a-guide-to-enabling-business-central-only-access-using-network-security-perimeter/)