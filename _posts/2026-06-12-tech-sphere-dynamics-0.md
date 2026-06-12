---
layout: post
title: "Tech Sphere Dynamics: The Invisible Curve: When AI Subscriptions Stop Adding Up"
published: true
original_date: 2026-04-22
---

Verdikt: NE – Text pouze obecně popisuje konec flat-rate předplatných u AI vendorů (Anthropic, GitHub, SAP) bez jakéhokoliv konkrétního dopadu na AL vývoj nebo nové featury v Business Central.

<!--více-->

- Posun AI vendorů od flat-rate k token-based/consumption modelům indikuje nutnost optimalizace AL integrací (HttpClient volání na Azure OpenAI/Anthropic APIs) s důrazem na minimalizaci tokenů a precizní context window management.
- Architektura Copilot integrací v BC se musí adaptovat na asynchronní zpracování a lokální validaci dat přímo v AL před odesláním payloadu, aby se zamezilo redundantním a nákladným API dotazům.
- Trend směřuje k orchestraci autonomních AI agentů mimo BC sandbox (např. přes Azure platformu), přičemž AL bude sloužit primárně jako transakční vrstva poskytující strukturovaná data přes OData/API a exekuční endpoint pro callbacky.

[Číst celý článek](https://techspheredynamics.com/2026/04/22/the-invisible-curve-when-ai-subscriptions-stop-adding-up/)