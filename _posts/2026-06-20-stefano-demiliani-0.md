---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central: download symbols from Microsoft’s public NuGet source."
published: true
original_date: 2026-02-23
---

Verdikt: ANO – Článek přináší zásadní informaci pro modernizaci CI/CD pipelines, protože popisuje možnost stahování AL symbolů přímo z veřejného NuGet registru Microsoftu bez nutnosti běžící BC instance.

<!--více-->

- Microsoft začal publikovat systémové a aplikační AL symboly (System Application, Base Application) jako standardní NuGet balíčky ve svém veřejném repozitáři, což nahrazuje tradiční stahování přes `al.downloadSymbols` z lokálního sandboxu či Docker kontejneru.
- Tento přístup umožňuje plně bezkontejnerovou kompilaci (containerless builds) v GitHub Actions nebo Azure DevOps, čímž se dramaticky zrychluje spouštění buildů a statické analýzy kódu (AppSourceCop) díky eliminaci režie spojené se startem BC kontejneru.
- V praxi stačí nakonfigurovat `nuget.config` s příslušným zdrojem od Microsoftu a použít NuGet CLI / dotnet restore pro stažení `.app` souborů jako závislostí přímo do lokální složky `.alpackages` před spuštěním AL kompilátoru.

[Číst celý článek](https://demiliani.com/2026/02/23/dynamics-365-business-central-download-symbols-from-microsofts-public-nuget-source/)