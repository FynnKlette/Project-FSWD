---
title: Danial Banitorfi
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
# Danial Banitorfi

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

[1,3]

### Personal goals

[My goal is to understnd the architecture behind Web-Dev. and gain real experience in the Full-Stack-Dev. workflow which includes working with Python, Flask etc., as well as coding as a team.]

---

## Eidesstattliche Erklärung

**[Danial Banitorfi, Matrikelnr.: 77209870745]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Login| the way the login login interacts with the database | my difficulty to work with the database | 
| 2 | Sign up |making sure that the data is stored in the database with specific formats | The challange of understanding how the HTML logic cooperates with the rest of the backend  |
| 3 | Studbüro login| creting data in advance that works when one types it in, in oder to gain acces to a exclusive page  | getting used to understand sql syntax in a python file  |

## Design Decisions that I led

1. [DD #03](../design-decisions/dd-03.md)
2. [DD #04](../design-decisions/dd-04.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| [Design Challenge research] | [Research traces](../product-discovery/01-design-challenge.md#raw-materia) | See left |
| [Refactor to use Flask Blueprints] | [Commit 1](https://github.com/hwrberlin/fswd/commit/d816e4), [Commit 2](https://github.com/hwrberlin/fswd/commit/75a6c1) | [Flask Documentation](https://flask.palletsprojects.com/en/stable/blueprints/#the-concept-of-blueprints) |
| starting pages | commits 1-2| Flask Documentation, |
| validators | commits 3-4 | Flask Documentation-WTForms |
| sign up and login (front and backend)  | commits 3-10  | Flask Documentation-SQL and lecture |
| login studbüro | commits 6-10 |   |
| app.py correction| commits 7-16 |  |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | ChatGPT| explaining basic rundowns as to how flash routes work in order to combine python logic with html syntax |login.py ( neuer Name loginbp.) |explain to me how a button in HTML is received as an action and ignites into a method. |
| 02  |  Gemini |Jinja syntax explaining | login.py, show/regsiter.html | The flash messages e .g had to be shown implemented into html and i use| 
| 03 | Gemini | how i hash a password for the login logic| login.py|  getting to know how bcrypt works and how i could implement it into my methods|
| 04 | Gemini | explanation with reason| login.py, app.py|  understanding how  the sessions and the assigned roles of them work and how i could combine that logic of the login_manager |

