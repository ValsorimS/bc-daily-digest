---
layout: post
title: "Stefano Demiliani: Be careful with Visual Studio Code extensions…"
published: true
original_date: 2026-05-21
---

**Verdikt:** ANO.

<!--více-->

2.  *   **VS Code Security Breach Impact na AL:** GitHub byl postižen bezpečnostním narušením skrze malware vložený do VS Code rozšíření. Pro AL vývojáře je to kritické, protože Visual Studio Code je primární integrované vývojové prostředí (IDE) pro vývoj Business Central AL aplikací a využívá rozsáhlé spektrum rozšíření.
    *   **Technické detaily a rizikový vektor:** Malware v rozšíření představuje přímý vektor pro supply chain útoky na AL vývojový stack. Může vést ke kompromitaci zdrojového kódu, přihlašovacích údajů, CI/CD pipeline tokenů nebo k distribuci škodlivého kódu v rámci AL projektů. Specifické techniky malwaru nejsou uvedeny, ale obecně jde o exekuci libovolného kódu s oprávněními vývojáře.
    *   **Trends & Mitigation pro AL:** Aktuálním trendem je zvýšený důraz na DevSecOps principy a security governance v rámci vývojového cyklu. Pro AL doporučujeme implementaci přísných politik pro správu a auditování VS Code rozšíření, verifikaci jejich zdrojového kódu (je-li open-source) a integraci nástrojů pro statickou analýzu kódu a skenování závislostí do AL build pipelines pro detekci potenciálních zranitelností a malwaru v dodavatelském řetězci.

[Číst celý článek](https://demiliani.com/2026/05/21/be-careful-with-visual-studio-code-extensions/)