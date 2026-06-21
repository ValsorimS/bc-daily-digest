---
layout: post
title: "Stefano Demiliani: Azure Logic Apps: never share the same storage account between different apps."
published: true
original_date: 2026-02-04
---

Verdikt: ANO – Článek přináší kritické varování před sdílením Azure Storage účtu mezi integračními službami, což přímo ovlivňuje stabilitu a spolehlivost BC konektorů.

<!--více-->

- Sdílení jednoho Azure Storage Accountu mezi více instancemi Azure Logic Apps (Standard) nebo Azure Functions způsobuje kolize Host ID a konflikty v distribuovaném zamykání (blob/queue leasing).
- V BC integracích a u externích AI agentů postavených na serverless architektuře vede tato konfigurace k selhání triggerů, ztrátě zpráv v queue a nepředvídatelným pádům při asynchronním volání z AL kódu.
- Jako best practice je vyžadována striktní izolace (dedikovaný Storage Account pro každou Logic App/Function) nebo manuální redefinice unikátního ID hostitele v `host.json` pro zamezení konfliktů v metadatech úložiště.

[Číst celý článek](https://demiliani.com/2026/02/04/azure-logic-apps-never-share-the-same-storage-account-between-different-apps/)