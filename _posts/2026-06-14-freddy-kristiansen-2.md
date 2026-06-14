---
layout: post
title: "Freddy Kristiansen: Branching strategies for your AL-Go for GitHub repo"
published: true
original_date: 2022-05-03
---

Verdikt: ANO – Článek definuje kritické strategie větvení v AL-Go for GitHub, které jsou klíčové pro správné nastavení moderních CI/CD pipelines v Business Central.

<!--více-->

- Integrace standardizovaných Git branching strategií (např. GitHub Flow) přímo do ekosystému AL-Go for GitHub pro zajištění izolace vývoje a stability master/main větve.
- Konfigurace automatizovaných GitHub Actions pro validaci PR (Pull Requests), kompilaci AL kódu a spouštění regresních testů v BC Docker kontejnerech před sloučením kódu.
- Řízení životního cyklu AL aplikací pomocí automatického verzování (version bumping) a řízeného deploymentu do různých Business Central SaaS prostředí (Dev, QA, Prod) definovaných v konfiguračním souboru settings.json.

[Číst celý článek](https://freddysblog.com/2022/05/03/branching-strategies-for-your-al-go-for-github-repo/)