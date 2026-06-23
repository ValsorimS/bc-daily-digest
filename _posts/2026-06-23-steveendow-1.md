---
layout: post
title: "Steveendow: Power Automate Business Central Journal Line Import Error"
published: true
original_date: 2022-04-22
---

Verdikt: NE – Článek řeší specifickou integrační chybu Power Automate konektoru pro D365BC při zápisu General Journal Lines, nikoli novinky v AL, AI agenty ani obecné technické trendy.

<!--více-->

*   Popisuje chybu `Application_DialogException` s hláškou "You must specify a journal batch ID or a journal ID to get a journal line" při pokusu o vložení záznamu `General Journal Line` přes `Power Automate Create Record (V3)` akci.
*   Problém spočívá v nutnosti explicitního předání `Journal Batch ID` nebo `Journal ID` při vytváření podřízeného záznamu, což reflektuje validační logiku D365BC API pro účetní deníky.
*   Nejedná se o novou technologii či AL funkcionalitu, ale o specifickou interakci mezi Power Automate konektorem a D365BC API z dubna 2022, vyžadující správné strukturování dat.

[Číst celý článek](https://blog.steveendow.com/2022/04/power-automate-business-central-journal.html)