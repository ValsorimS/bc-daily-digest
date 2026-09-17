---
layout: post
title: "VS Code Blog: Building the new GitHub Copilot Inline Suggestions Model: Part One"
published: true
original_date: 2026-09-16
---

Verdikt: ANO – Článek vysvětluje novou sjednocenou architekturu inline návrhů Copilotu ve VS Code, která zásadně zrychluje a zpřesňuje predikci kódu i víceřádkový refaktoring během vývoje v AL.

<!--více-->

- Sjednocení tokenové predikce (inline completion), predikce další editace (next edit) a vzdálených kontextových návrhů (long-distance suggestions) do jednoho společného modelu namísto dřívějšího řetězení izolovaných modelů.
- Optimalizace inference a dramatické snížení latence ve VS Code prostředí, což eliminuje prodlevy při doplňování syntaxe a symbolů v AL.
- Schopnost modelu udržet širší kontext pro predikci navazujících změn na více místech současně, klíčová pro komplexnější úpravy napříč AL objekty (např. synchronní úpravy procedur v codeunitách a volání v page extensions).

[Číst celý článek](https://code.visualstudio.com/blogs/2026/09/16/building-the-github-copilot-inline-suggestions-model-part-one)