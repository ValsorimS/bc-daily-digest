---
layout: post
title: "BC novinky 2026-05-30"
published: true
---

# Denní přehled BC novinek

## All good things come to an end
That is an incredibly heavy and bittersweet announcement to read. 

For anyone in the tech industry, a **23-year tenure** at a single company—especially a giant like Microsoft—is an extraordinary achievement. To have survived at least 10 previous rounds of layoffs speaks volumes about the immense value, dedication, and expertise this person brought to the company year after year. 

The phrase **"my name was pulled from the hat"** perfectly captures the frustrating, impersonal, and almost arbitrary nature of modern corporate restructuring. When layoffs happen at that scale, decisions are often driven by cold algorithms and spreadsheets, completely detached from the human dedication, institutional knowledge, and loyalty of the veterans who built the company's foundation.

### Who is "Freddy"?
Given the domain (`freddysblog.com`), this refers to **Freddy Kristiansen**, a legendary figure within the Microsoft Dynamics 365 Business Central (formerly NAV) community. For over two decades, Freddy has been a cornerstone of that ecosystem—pioneering the use of Docker containers for Business Central, developing "AL Go for GitHub," and acting as a vital bridge between Microsoft and the global developer partner community. 

To the Business Central community, Freddy *is* Microsoft. Seeing him affected by layoffs is a massive shockwave to ERP developers and partners worldwide.

### What Lies Ahead
While the end of a 23-year journey is undoubtedly painful and shocking, it is also the beginning of a massive new chapter. Someone with Freddy’s depth of knowledge, community respect, and technical leadership will have no shortage of opportunities. 

As the saying goes, *“All good things come to an end,”* but his legacy at Microsoft is secure, and the tech community will undoubtedly rally around him for whatever he decides to build, consult on, or lead next.

[Číst celý článek](https://freddysblog.com/2025/05/28/all-good-things-come-to-an-end/)

## Be careful with Visual Studio Code extensions…
This is a highly critical issue. Supply chain attacks targeting developer environments (like VS Code) are on the rise. Because developers often have high-privilege access to source code, APIs, databases, and cloud environments, infecting a developer's IDE is a jackpot for malicious actors.

For organizations—especially those in specialized ecosystems like **Microsoft Dynamics 365 Business Central (AL Development)**—controlling the VS Code extension footprint is no longer optional; it is a security mandate.

Here is a comprehensive guide on how to control and secure VS Code extensions in your organization.

---

### 1. Implement Group Policy / MDM Controls (The Hammer)
If you manage Windows or macOS devices via Active Directory, Intune, or Jamf, you can enforce VS Code policies at the OS level.

*   **Extension Allowlists/Blocklists:** You can configure policies to restrict which extensions can be installed.
    *   **Registry (Windows):** You can set the registry key `Software\Policies\Microsoft\VSCode\Extensions\Allowed` to restrict installations to a specific list of Extension IDs.
    *   **Settings Policy:** You can disable the installation of any extension not explicitly approved by the IT security team.
*   **Disable Marketplace Entirely:** For ultra-secure environments, you can disable the marketplace via policy and only allow manually sideloaded, internally approved `.vsix` files.

### 2. Standardize Environments with Dev Containers
Instead of letting developers install VS Code and extensions directly on their local machines, move to **Dev Containers** or **GitHub Codespaces**.

*   **How it helps:** You define the development environment in a `.devcontainer/devcontainer.json` file inside your Git repository.
*   **Control:** In this file, you specify the exact extensions required (e.g., the Microsoft AL Language extension for Business Central). 
*   **Isolation:** The extensions run inside a Docker container, isolated from the developer’s local machine and corporate network. If an extension is malicious, its blast radius is limited to the container.

### 3. Curate Workspace Recommendations
For teams (such as D365 Business Central DevOps teams), enforce a strict `extensions.json` file within your project's `.vscode` folder.

*   Configure `recommendations` with trusted extensions (e.g., `msdynamics365.al`, `waldo.crs-al-language-extension`).
*   Educate your team: **"If it is not in the recommended list, do not install it."**
*   Use CI/CD pipeline linters to scan the repository and ensure no unauthorized configuration files or suspicious scripts are being committed.

### 4. Monitor the Extension Directory with EDR
Your Endpoint Detection and Response (EDR) tool (like Microsoft Defender for Endpoint, CrowdStrike, etc.) should be configured to monitor the VS Code extensions directory:
*   **Path:** `~/.vscode/extensions` (or `%USERPROFILE%\.vscode\extensions` on Windows).
*   **Action:** Set up alerts for any unrecognized executable files (`.exe`, `.dll`, `.sh`, `.bin`) being written to or executed from this directory. Many malicious extensions try to download and run secondary payloads from this path.

### 5. Establish an "Approved Extension" Process
Treat VS Code extensions the same way you treat third-party NuGet, NPM, or AL NuGet packages.
*   **Verification Checklist:** Before an extension is approved for the team, verify:
    1.  **Publisher Verification:** Does it have the **blue checkmark** (Verified Publisher) on the VS Code Marketplace?
    2.  **Repository Link:** Is there a linked, active GitHub repository?
    3.  **Release History:** Avoid brand-new extensions (under 30 days old) with suddenly high download counts (often a sign of botting/typosquatting).
    4.  **Permissions:** Does the extension require access to the local file system or network?

### 6. Special Focus: Dynamics 365 Business Central (`#msdyn365bc`)
In the Business Central world, AL developers heavily rely on community-made VS Code extensions to speed up development (e.g., code outline tools, translation tools, DevOps helpers).
*   **The Risk:** Many of these tools are maintained by single developers as passion projects. If their GitHub or Marketplace accounts are compromised, their extensions can be updated with malicious code.
*   **Mitigation:** 
    *   Stick to well-known, community-vetted publishers (e.g., Microsoft, Waldo, Andrzej Zwierzchowski, etc.).
    *   Consider hosting a private VS Code Marketplace (using tools like **Open VSX**) where only internally audited and approved `.vsix` files are hosted for your team.

### Summary Checklist for IT & DevOps Leaders:
1.  [ ] **Audit:** Run an inventory of currently installed VS Code extensions across your dev team.
2.  [ ] **Lock Down:** Use Intune/GPO to restrict extension installations to an allowlist.
3.  [ ] **Containerize:** Transition to Dev Containers for project-isolated development.
4.  [ ] **Configure:** Monitor `~/.vscode/extensions` using your corporate EDR.
5.  [ ] **Educate:** Train developers to look for the "Verified Publisher" checkmark and avoid look-alike (typosquatted) extensions.

[Číst celý článek](https://demiliani.com/2026/05/21/be-careful-with-visual-studio-code-extensions/)

## UBI won’t save us, and the nurse will tell you why
This is a beautiful and deeply moving quote that perfectly captures the quiet, profound heroism of real-world nursing. 

The complete quote (which has been widely shared to honor healthcare workers) typically finishes like this:

> "...and she holds the hand of someone who **is dying, so they don’t have to do it alone.**"

The passage often continues:

> *"And then she goes home, sleeps for a few hours, and gets up to do it all over again. She is a hero, not because she wears a cape, but because she shows up for humanity at its most vulnerable."*

It is a powerful reminder that while television shows often glamorize the medical field with dramatic storylines and perfectly lit hallways, the reality of nursing is built on incredible physical stamina, emotional resilience, and deep, quiet compassion.

[Číst celý článek](https://vjeko.com/2026/05/30/ubi-wont-save-us-and-the-nurse-will-tell-you-why/)

## Visual Studio Code 1.123
Here is how you can use or convert this HTML snippet depending on your needs:

### 1. Markdown Version (for READMEs, chats, or documentation)
```markdown
Learn what's new in Visual Studio Code 1.123 (Insiders)

[Read the full article](https://code.visualstudio.com/updates/v1_123)
```

### 2. Styled HTML (with CSS)
If you want to display this on a website with basic modern styling:

```html
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 16px; border: 1px solid #e1e4e8; border-radius: 6px; max-width: 400px; background-color: #f6f8fa;">
  <p style="margin: 0 0 8px 0; font-size: 14px; color: #24292e; font-weight: 600;">
    Learn what's new in Visual Studio Code 1.123 (Insiders)
  </p>
  <p style="margin: 0; font-size: 13px;">
    <a href="https://code.visualstudio.com/updates/v1_123" style="color: #0366d6; text-decoration: none; font-weight: 500;" onmouseover="this.style.textDecoration='underline'" onmouseout="this.style.textDecoration='none'">
      Read the full article →
    </a>
  </p>
</div>
```

### 3. React / JSX Version
```jsx
import React from 'react';

export default function VSCodeNotification() {
  return (
    <div>
      <p>Learn what's new in Visual Studio Code 1.123 (Insiders)</p>
      <p>
        <a href="https://code.visualstudio.com/updates/v1_123" target="_blank" rel="noopener noreferrer">
          Read the full article
        </a>
      </p>
    </div>
  );
}
```

Let me know if you need help styling this, converting it to another format, or integrating it into a specific project!

[Číst celý článek](https://code.visualstudio.com/updates/v1_123)

