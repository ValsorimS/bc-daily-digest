---
layout: post
title: "Stefano Demiliani: Azure Functions: never share the same storage account between function apps."
published: true
original_date: 2026-02-03
---

Verdikt: ANO – Článek popisuje kritické riziko sdílení jednoho Storage Accountu mezi více Azure Function Apps, což fatálně ovlivňuje spolehlivost externích integrací Business Central.

<!--více-->

* Sdílení nastavení `AzureWebJobsStorage` způsobuje kolize Host ID (generovaných z názvu aplikace a zkrácených na 32 znaků) a konflikt v distribuovaném zamykání přes Blob leases, což vede k selhání Timer a Queue triggerů.
* V BC architektuře (např. při offloadování AL procesů přes HttpClient nebo při integraci AI agentů běžících jako microservices) toto sdílení způsobuje náhodné mizení zpráv ve frontách, duplicitní spouštění nebo tiché zablokování webhooků.
* Správným řešením je striktní izolace – každá Function App musí mít v bicep/ARM šablonách pro CI/CD definovaný vlastní unikátní Storage Account pro `AzureWebJobsStorage` i `WEBSITE_CONTENTAZUREFILECONNECTIONSTRING`.

[Číst celý článek](https://demiliani.com/2026/02/03/azure-functions-never-share-the-same-storage-account-between-function-apps/)