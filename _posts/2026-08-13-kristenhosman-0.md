---
layout: post
title: "kristenhosman: Run Consolidation: There is no Business Unit to consolidate - Report Settings"
published: true
original_date: 2026-08-13
---

Verdikt: NE – Článek řeší pouze triviální uživatelský problém s nastavením sestavy a nepřináší žádné technické novinky v AL, AI agentech ani trendy.

<!--více-->

- Chyba „There is no Business Unit to consolidate“ vzniká v Page 242 „Consolidate Wizard“ na triggeru `Finalize - OnAction` (Base App v26.5) a izolovaně postihuje jednoho uživatele.
- Příčinou selhání jsou neplatná nebo poškozená uložená data parametrů sestavy v systémové funkcionalitě uložení definic.
- Problém se řeší odstraněním odpovídajících záznamů v relaci k danému Report ID z tabulky Report Settings.

[Číst celý článek](https://www.kristenhosman.com/2026/08/run-consolidation-there-is-no-business.html)