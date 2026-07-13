---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central: the mistery around the “Parallel Session Management” codeunit."
published: true
original_date: 2026-07-13
---

Verdikt: ANO – Článek odkrývá skryté pozadí a možnosti využití systémové Codeunit 490 (Parallel Session Management) pro efektivní řízení asynchronních procesů v AL.

<!--více-->

- Codeunit 490 slouží jako interní mechanismus platformy pro správu a limitování paralelně běžících relací (Background Sessions), což pomáhá předcházet throttling limitům v SaaS prostředí.
- Objekt zapouzdřuje logiku pro bezpečné spouštění asynchronních úloh přes `STARTSESSION` a `TASKSCHEDULER`, přičemž dynamicky vyhodnocuje aktuální zátěž a dostupnost systémových prostředků (vláken).
- Pro AL vývojáře je pochopení této codeunity klíčové při návrhu high-throughput integrací a hromadných operací, kde je nutné optimalizovat concurrency a eliminovat blokování databáze (locking).

[Číst celý článek](https://demiliani.com/2026/07/13/dynamics-365-business-central-the-mistery-around-the-parallel-session-management-codeunit/)