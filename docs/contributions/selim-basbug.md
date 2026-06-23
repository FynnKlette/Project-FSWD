---
title: Selim Basbug
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
# Selim Basbug

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

My target grade is 1,7 because i think it is an achievable and realistic target goal.

### Personal goals

My personal goal in regards of this Module is to extend my existing knowledge about Flask, Python and web-dev 

---

## Eidesstattliche Erklärung

**[Selim Basbug, Matrikelnr.: 77205089527]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | i made the entire functionality for the studienburo: the csv_upload, listing of courses/modules in db and listing of the tausch table | i had no issues while coding, did not use any ai | sometimes i made little spelling / syntax mistakes with took me some time to find |
| 2 | made the global_tauschfindung method in tausch.py | i thought it would be complicated; it wasnt| had to trail error alot |
| 3 | copied login_required into studburo_required  | did my own logic with the db query and it worked | import EEXCEMPT_METHODS didnt work so i clicked trough the modules and it was just a string i could copy into my own decorator :> |

| 3 | tried my best to make everyones work together | it worked in the end after days with small sleep and small freetime | understanding took some time of the code from my teampatners |
| 4 | /profile_api view | i got it working in 5mins | i tought just return jsonfiy(current_user) would work but i had to look up all current_user. endings for json thigns and fortunely tired __dict__ and it worked |
| 5 | made the clear db function | did my own logic with the db query and it worked | / |
| 7 | made dummy.py to work on tausch.py while teampatners worked on implementing kursabgabe.py | its just a debug module but tested some sql | / |

## Design Decisions that I led

1. [DD #00](../design-decisions/dd-07.md)
2. [DD #01](../design-decisions/dd-08.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| manually created fb1.csv trough Vorlesungsverzeichnis on S.A.M by copying the raw html and making an csv out of it | | https://sam.hwr-berlin.de/de/vorlesungsverzeichnis.php , https://www.w3schools.com/sql/ , https://docs.python.org/3/library/io.html|
| created and maintained csv_upload module and studienburo module|  | / |
| created and maintained studburo_req module |  | login_required module copied |
| created and maintained tausch, dummy, db_reinigen and db_update modules |  | https://www.w3schools.com/sql/ |
| made each module of project into a blueprint and added to app.py |  | https://flask.palletsprojects.com/en/stable/blueprints/ |
| added profile, upload_csv, profil, profile_api, dashboard views to app.py |  | https://flask-json.readthedocs.io/en/latest/index.html |
| configured jinja all templates of project to work with base and base_sb templates correctly | | https://jinja.palletsprojects.com/en/stable/templates/|
| corrected UserMixin user data to contain all data except password | | https://flask-login.readthedocs.io/en/latest/ |
---

i have too many commits to paste each one. Apologies!

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  |         |                |                                 |                             |
| 02  |         |                |                                 |                             |
| ... |         |                |                                 |                             |
