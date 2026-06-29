---
layout: post
title: "VS Code Blog: Context is all you need: Better AI results with custom instructions"
published: true
original_date: 2025-03-26
---

Verdikt: ANO – Článek představuje GA verzi uživatelských instrukcí pro VS Code Copilot, což je klíčové pro automatické přizpůsobení AI asistentů specifickým standardům vývoje v AL.

<!--více-->

- Obecná dostupnost (GA) Custom Instructions umožňuje definovat systémové prompty na úrovni uživatele nebo workspace (pomocí souboru `.github/copilot-instructions.md`), které globálně ovlivňují chování GitHub Copilot ve VS Code.
- Pro AL vývoj to umožňuje striktně definovat pravidla pro generování kódu, jako je vynucení AppSourceCop a Runtime pravidel, správné struktury AL objektů (např. oddělení business logiky od tabulkových triggerů) nebo specifické konvence pro pojmenovávání proměnných.
- Integrace funguje napříč VS Code Chat a Inline Chat, což v praxi vytváří lokálního AI agenta, který automaticky refaktoruje a generuje AL kód v souladu s firemními best practices bez nutnosti opakovaného zadávání kontextu.

[Číst celý článek](https://code.visualstudio.com/blogs/2025/03/26/custom-instructions)