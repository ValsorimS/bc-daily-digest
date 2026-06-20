---
layout: post
title: "Steveendow: My New Criteria for a Password Manager"
published: true
original_date: 2022-12-27
---

Verdikt: NE – Text se vůbec netýká vývoje v AL, AI agentů ani platformy Business Central, ale analyzuje bezpečnostní incident a kryptografické slabiny správce hesel LastPass z roku 2022.

<!--více-->

- Architektura datového trezoru LastPass nešifruje metadata a URL adresy uložených záznamů, což útočníkům po úniku záloh umožňuje provádět pasivní analýzu cílů a strukturovaný phishing.
- Kryptografické odvození klíče (KDF) u účtů vytvořených před rokem 2018 využívá pouze legacy konfiguraci s 5 000 iteracemi PBKDF2 namísto bezpečnějších 100 100 iterací, což kriticky snižuje výpočetní náročnost offline brute-force útoků na master password.
- Poskytovatel neprováděl automatickou migraci starších šifrovaných databází (vaultů) na silnější bezpečnostní standardy a zpětně nevynucoval striktní politiku minimální entropie hlavního hesla.

[Číst celý článek](https://blog.steveendow.com/2022/12/my-new-criteria-for-password-manager.html)