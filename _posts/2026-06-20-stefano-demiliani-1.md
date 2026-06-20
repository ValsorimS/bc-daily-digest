---
layout: post
title: "Stefano Demiliani: Dynamics 365 Business Central: BCMCPProxy vNext"
published: true
original_date: 2026-02-13
---

Verdikt: ANO – Článek je zásadní pro pochopení toho, jak integrovat AI agenty přímo s AL API pomocí nového standardu MCP (Model Context Protocol) a nástroje `bcmcpproxy`.

<!--více-->

- Microsoft vydal open-source proxy `bcmcpproxy` (vNext) implementující Model Context Protocol (MCP), což umožňuje LLM agentům (např. Claude, Copilot) přímo a obousměrně komunikovat s Business Central.
- Proxy automaticky mapuje standardní i custom API stránky a API dotazy (Queries) definované v AL na MCP "Tools" (nástroje pro akce) a "Resources" (zdroje dat), které pak LLM dokáže dynamicky objevovat, číst a zapisovat přes OData/REST v reálném čase.
- Architektura staví na OAuth2 autentizaci vůči BC SaaS, odstiňuje vývojáře od složité orchestrace LLM a transformuje AL business logiku na bezpečně volatelná API schémata přímo interpretovatelná AI modely.

[Číst celý článek](https://demiliani.com/2026/02/13/dynamics-365-business-central-bcmcpproxy-vnext/)