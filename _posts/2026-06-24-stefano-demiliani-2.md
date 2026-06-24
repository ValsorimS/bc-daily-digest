---
layout: post
title: "Stefano Demiliani: Do you have applications connecting to an Azure Storage Account? Be sure to use TLS 1.2 or later."
published: true
original_date: 2026-01-14
---

Verdikt: NE – Článek se primárně týká infrastruktury Azure a požadavků na TLS, neobsahuje novinky pro AL, AI agenty ani specifické BC trendy.

<!--více-->

*   Azure Blob Storage bude od 3. února 2026 striktně vyžadovat TLS 1.2 nebo novější pro všechna připojení, což znamená kompletní deprecaci TLS 1.0 a 1.1.
*   Pro vlastní AL implementace v Dynamics 365 Business Central, které interagují s Azure Storage účty (např. pomocí `HttpClient` pro REST API volání), je klíčová kompatibilita hostujícího prostředí. Na on-premise BC je nutné zajistit, aby operační systém (Windows Server) podporoval a měl aktivovaný TLS 1.2 jako výchozí protokol pro odchozí komunikaci.
*   Ačkoli se nejedná o změnu v AL jazyce ani syntaxi, nepřímý dopad je na operativní aspekty. Řešení Business Central SaaS jsou zajištěna Microsoftem; on-premise implementace vyžadují administrátorskou kontrolu OS konfigurace protokolů TLS. Případné .NET interop volání využívající `ServicePointManager.SecurityProtocol` by měla explicitně nastavit `SecurityProtocolType.Tls12`.

[Číst celý článek](https://demiliani.com/2026/01/14/do-you-have-applications-connecting-to-an-azure-storage-account-be-sure-to-use-tls-1-2-or-later/)