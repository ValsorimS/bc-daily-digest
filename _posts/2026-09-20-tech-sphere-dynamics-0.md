---
layout: post
title: "Tech Sphere Dynamics: Agents vs Skills: Between the Agentic Monolith and Agentic Bureaucracy"
published: true
original_date: 2026-09-20
---

Verdikt: ANO – Článek přináší zásadní architektonický vhled do návrhu AI agentů v Business Central a varuje před neefektivní fragmentací systému na příliš mnoho autonomních actorů.

<!--více-->

- Architektonický odklon od hyper-specializovaných mikro-agentů ke konsolidovaným actorům s více nástroji (tool-calling skills v AL), což redukuje latenci orchestrace a zbytečnou složitost agentních stavových automatů.
- Definice striktních context boundaries a využití ALDC Graphu pro izolaci systémového stavu, zamezení degradace promptu a optimalizaci spotřeby tokenů v business procesech.
- Kritické vyhodnocení režie agentních systémů (cost of complexity) oproti deterministickému kódu v AL; doporučení ponechat jádro transakční logiky v AL a agenty nasazovat výhradně tam, kde je nedeterministické uvažování nezbytné.

[Číst celý článek](https://techspheredynamics.com/2026/09/20/agents-vs-skills-agentic-monolith-bureaucracy/)