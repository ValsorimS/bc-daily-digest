---
layout: post
title: "Stefano Demiliani: AI and prompt injections: the invoice that approves itself."
published: true
original_date: 2026-11-13
---

Verdikt: ANO – Článek se zaměřuje na kritické bezpečnostní riziko AI agentů, prompt injection, relevantní pro integrace v Business Central.

<!--více-->

*   Identifikace prompt injection jako zásadní bezpečnostní hrozby pro AI agenty, aplikovanou v kontextu automatizace procesů jako je schvalování faktur v Business Central.
*   Demonstrace zneužitelnosti AI agenta vložením imperativních instrukcí přímo do datového vstupu (např. do popisu faktury), což může vést k obcházení schvalovacích workflow a nepovolené automatické akci (např. samo-schválení faktury AI).
*   Zásadní důsledek pro AL vývojáře je nutnost implementace robustních sanitizačních a validačních mechanizmů pro všechny vstupy směřující k AI modelům, vč. zvážení použití služeb jako Azure AI Content Safety a principů defense-in-depth pro ochranu integrity AI chování a dat Business Central.

[Číst celý článek](https://demiliani.com/2026/11/13/ai-and-prompt-injections-the-invoice-that-approves-itself/)