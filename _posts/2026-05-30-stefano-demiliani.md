---
layout: post
title: "Stefano Demiliani: Be careful with Visual Studio Code extensions…"
published: true
---

# Be careful with Visual Studio Code extensions…

Zde je vysoce technické shrnutí incidentu se zaměřením na vývoj v MS Dynamics 365 Business Central a moderní trendy:

*   **Kompromitace AL dodavatelského řetězce (Supply Chain):** Jelikož je VS Code výhradním IDE pro AL vývoj, napadení jeho ekosystému přímo ohrožuje citlivá data BC projektů. Útočníci mohou přes škodlivé extenze exfiltrovat přihlašovací údaje k SaaS/On-Prem environmentům z `launch.json`, kompromitovat lokální BC licencování nebo modifikovat AL Go pipeline v rámci CI/CD (GitHub Actions/Azure DevOps).
*   **Riziko pro AI agenty a LLM integrace:** Moderní AL programování stále více spoléhá na AI asistenty (GitHub Copilot, lokální LLM extenze). Malware ve VS Code může manipulovat s kontextem AI (prompt injection), krást proprietární AL kód odesílaný do LLM API, případně zneužít API klíče k podnikovým kognitivním službám integrovaným přímo v editoru.
*   **Nezbytnost DevSecOps a DevContainers:** Reakcí na tuto hrozbu je opuštění nekontrolovaných lokálních instalací VS Code. Pro AL vývoj je nutné implementovat striktní politiky správy extenzí (allowlisty) a přejít na izolovaná vývojová prostředí pomocí **DevContainers** či GitHub Codespaces, která omezují oprávnění doplňků k lokálnímu OS a síťovým prostředkům.

[Číst celý článek](https://demiliani.com/2026/05/21/be-careful-with-visual-studio-code-extensions/)