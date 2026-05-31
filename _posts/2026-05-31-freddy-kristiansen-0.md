---
layout: post
title: "Freddy Kristiansen: Invoke-ScriptInBcContainer"
published: true
---

1.  **Verdikt:** NE, protože se článek zaměřuje na specifické, zastaralé změny ve funkci `Invoke-ScriptInBcContainer` v `BcContainerHelper` z roku 2022 a neobsahuje informace o AL, AI agentech nebo aktuálních trendech v Business Central.

2.  **Technické shrnutí:**
    *   Funkce `Invoke-ScriptInBcContainer` v PowerShell modulu `BcContainerHelper` prošla zásadními změnami ve verzi 3.0.9 (vydané v květnu 2022).
    *   Tato funkce umožňuje spouštění libovolných PowerShell `scriptblock`ů přímo uvnitř zadaného Business Central Docker kontejneru, s parametry jako `containerName` a `scriptblock`.
    *   Zásadní změny vyžadují revizi stávajících automatizačních skriptů a CI/CD pipeline, které tuto funkci využívají, s cílem zajistit kompatibilitu a optimalizovat workflow pro práci s kontejnery.

[Číst celý článek](https://freddysblog.com/2022/05/24/invoke-scriptinbccontainer/)