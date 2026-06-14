---
layout: post
title: "Steveendow: Business Central Simple Tip #5:  Comment Lines, Standard Text Codes, and Extended Text"
published: true
original_date: 2023-06-01
---

Verdikt: NE – Článek popisuje pouze elementární, dlouhodobě existující uživatelské funkce komentářů a standardních textů, takže pro zkušeného BC vývojáře nepřináší žádné nové technické informace, AL kód ani pohled na moderní trendy.

<!--více-->

- Použití typu řádku "Comment" pro ad-hoc textové zápisy přímo v řádcích prodejních a nákupních dokladů bez vazby na standardní entity (zboží, zdroje, věcné účty).
- Hardkodované omezení délky pole Description na maximálně 100 znaků pro komentáře a standardní texty, což pro delší textace vyžaduje řetězení řádků nebo využití tabulek a logiky Extended Text.
- Standard Text Codes s limitem 20 znaků pro kód (Code[20]) fungující jako systémové šablony vkládané přes validační logiku pole "No.", jež lze v AL rozšiřovat přes standardní table/page extension nad objekty "Standard Text".

[Číst celý článek](https://blog.steveendow.com/2023/06/business-central-simple-tip-5-comment.html)