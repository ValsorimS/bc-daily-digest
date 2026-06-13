---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central: new strict URI validation in AL Http Client"
published: true
original_date: 2026-04-02
---

Verdikt: ANO – Přináší zásadní informaci o breaking change ve validaci URI v AL HttpClient ve verzi 28, která může okamžitě znefunkčnit vaše stávající integrace.

<!--více-->

- AL HttpClient v BC v28 (2026 Wave 1) zavádí striktní validaci URI podle standardů RFC, což nahrazuje dosavadní benevolentní parsování adres.
- Neescapované znaky a nestandardní query parametry v HTTP požadavcích nově vyvolají runtime chybu, takže je nutné refaktorovat kód a explicitně používat encoding (např. přes `TypeHelper.UriEscapeDataString`).
- Změna zapadá do trendu celkového zpřísňování zabezpečení a stability AL runtime, kde Microsoft vynucuje striktní typování a validace na úkor zpětné kompatibility.

[Číst celý článek](https://demiliani.com/2026/04/02/dynamics-365-business-central-new-strict-uri-validation-in-al-http-client/)