---
layout: post
title: "Stefano Demiliani: The hidden cost of asking AI to do everything…"
published: true
original_date: 2026-07-21
---

Verdikt: ANO – Článek varuje před riziky „vibe codingu“ v AL a ukazuje, proč bezhlavé delegování vývoje na AI generuje masivní technický dluh v architektuře Business Central.

<!--více-->

- Nekritické generování AL kódu pomocí AI často ignoruje platformová specifika BC, což vede k anti-patternům jako je zneužívání tabulkových triggerů pro komplexní business logiku, ignorování `Partial Records` (JIT load) nebo neefektivním databázovým dotazům bez optimálního indexování a SIFT.
- Vygenerovaný kód postrádá hluboké porozumění transakčnímu modelu Business Central, což se projevuje nesprávným scope transakcí, nadbytečným voláním `Modify(true)` a generováním deadlocků v high-concurrency prostředích, což drasticky zvyšuje náklady na debugging a refaktorizaci.
- Role AL vývojáře se posouvá od psaní syntaxe k architektuře a auditu; klíčovou kompetencí se stává definování striktních guardrails pro AI agenty, validace návrhových vzorů (Design Patterns), analýza telemetrie v Application Insights a enforcement pravidel AppSource Copu.

[Číst celý článek](https://demiliani.com/2026/07/21/the-hidden-cost-of-asking-ai-to-do-everything/)