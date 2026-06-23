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

##Contributions
| Contribution | Proof, e.g., git commits | Sources used |
|---|---|---|
| Kursabgabe Module — Flask App, erste Route GET /abgaben | [e09b13a](https://github.com/FynnKlette/Project-FSWD/commit/80f4fa1) | Flask Docs |
| Kursabgabe — SQLite DB-Verbindung für Abgaben | [5068c37](https://github.com/FynnKlette/Project-FSWD/commit/5068c37) | Flask Docs, SQLite Docs |
| Kursabgabe — WTForms Formular, Template, Route /abgaben/neu | [d431d0d](https://github.com/FynnKlette/Project-FSWD/commit/d431d0d), [f0f988d](https://github.com/FynnKlette/Project-FSWD/commit/f0f988d) | WTForms Docs |
| Kursabgabe — POST/INSERT, PRG Pattern, Flash, Wartelisten-Sortierung | [7e717dd](https://github.com/FynnKlette/Project-FSWD/commit/7e717dd), [a1fe6cc](https://github.com/FynnKlette/Project-FSWD/commit/a1fe6cc) | WTForms Docs, Flask Docs |
| Anfragen-Modul — AnfrageForm, Routes, Templates | [f461d7f](https://github.com/FynnKlette/Project-FSWD/commit/f461d7f) | WTForms Docs |
| Username-Validierung (studenten-Tabelle) + Duplikat-Prävention | [4b0ba39](https://github.com/FynnKlette/Project-FSWD/commit/4b0ba39) | SQLite Docs |
| Styled Flash Messages (grün/rot) | [5bea390](https://github.com/FynnKlette/Project-FSWD/commit/5bea390) | W3Schools |
| Repo-Struktur: Templates + kursabgabe.py in Root (Merge mit main) | [e09b13a](https://github.com/FynnKlette/Project-FSWD/commit/e09b13a) | – |
## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
|---|---|---|---|---|
| 01 | ChatGPT (OpenAI) | Bug fixing | Code (.py files) | Used to analyse error messages and related code snippets. The tool provided possible causes and likely locations of errors, and in some cases suggested solutions in the form of short code snippets. |
| 02 | DeepL Write | Wording and translation | Docs (DD-01, DD-02, this page) | Used to improve wording, grammar, and readability of documentation texts. The tool suggested alternative phrasings and corrections. |
