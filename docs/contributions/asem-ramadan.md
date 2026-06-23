---
title: Asem Ramadan
parent: Individual Contributions
nav_order: 1
---

{: .attention }
> Create a separate, individual file for every team member, proposed naming scheme: `📄firstname-lastname.md`.
>
> *Find and replace* (VS Code: <kbd>Ctrl</kbd>+<kbd>H</kbd> / <kbd>⌘</kbd>+<kbd>H</kbd>) `Jane Dane` with the student's name. On this template page, you will find this name 4 times (including in this `attention` box). 
>
> You may delete this `attention` box.

{: .no_toc }
# Asem Ramadan

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

1,7-2.0

### Personal goals

How a web app works. Git and GitHub teamwork. Python Flask, SQLite

---

## Eidesstattliche Erklärung
Asem Ramadan:77201310027

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| # | My contribution | Why I am proud of it | Which challenge I overcame |
|---|---|---|---|
| 1 | Built the Kursabgabe and Kursanfrage modules with Flask, WTForms, and SQLite. | It is the core matching functionality of the app. | Implementing full CRUD with form validation and the PRG pattern as a beginner. |
| 2 | Added user validation against the studenten table and duplicate protection per user/course. | Makes the app robust and protects the fairness of the waiting list. | Understanding where validation belongs (app vs. database). |
| 3 | Resolved merge conflicts during team refactoring (Blueprint structure, shared templates). | Learned real Git teamwork under pressure. | Working with merge conflicts and `--ours/--theirs` for the first time. |

## Design Decisions that I led

* [DD-05: Waiting List Principle (FIFO)](../design-decisions/dd-asem-01-wartelistenprinzip.md)
* [DD-06: Duplicate Protection](../design-decisions/dd-asem-02-duplikatschutz.md)

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
|---|---|---|
| Implemented `/abgaben` route with JOIN | PR #1, #2 | Flask Documentation, SQLite Docs |
| WTForms form for new submissions, POST + INSERT | PR #3 | Flask-WTF Documentation |
| PRG pattern with flash messages and ORDER BY zeitpunkt ASC | PR #3 | Flask Documentation |
| Mirrored logic for course requests (`/anfragen`) | PR #4 | — |
| User validation + duplicate protection | PR #4 | — |
| Styled flash messages (green/red) | PR #4 | — |
| Refactored module to team structure | PR #4 | — |

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
|---|---|---|---|---|
| 01 | ChatGPT (OpenAI) | Bug fixing | Code (.py files) | Used to analyse error messages and related code snippets. The tool provided possible causes and likely locations of errors, and in some cases suggested solutions in the form of short code snippets. |
| 02 | DeepL Write | Wording and translation | Docs (DD-01, DD-02, this page) | Used to improve wording, grammar, and readability of documentation texts. The tool suggested alternative phrasings and corrections. |
