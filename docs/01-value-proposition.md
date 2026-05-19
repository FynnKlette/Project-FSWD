---
title: Value Proposition
nav_order: 1
---

{: .no_toc }
# Value Proposition

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## The Problem

The main problem is the inefficient and confusing process of switching courses between students of the HWR trough unsorted Whatsapp Groups-Chats. That causes overspammed Whatsapp groups that make it hard to find a partner to switch with. 

The second problem is the inefficient and troublesome communication between the students with an aranged switch and the Studienbüro, which right now works trough sending an email with a document with the information of the students that want to switch courses. This leads to overspamming of Documents to the Studienbüro, that they have to painstakingly process these documents.

## Our Solution

Our solution provides a simple trade-like platform for the students that want to echange/trade specific courses with eachother. That way students can just easily find switching-partners and filter for people that want to switch the course they want and send a invite to change with them.

Also the Studienbüro that has an easier insight to the students that have already arranged an exchange and  can easily make the switch happen without breaking a sweat while reading trough a ton of individual documents.

## Target User(s)

- Bachelor-Students of the HWR Berlin, in the FB1, which want to switch their Courses with eachother.
- Studienbüro that wants to process the exchange of courses between students.

##  Happy Path

Situation 1 (student wants to sign up ) --> Calls up our Webapp --> is not signed in -->  clicks sign up button --> sign up form is called up --> inserts his information (like student email address, full name, matrikelnumber etc.) and presses sign up --> gets signed in

Situation 2 (student wants to insert switch offer ) --> must be logged in --> gets send to main page where they can see and filter existing switch offers --> presses create new offer button --> create offer form gets called up --> inserts the information (like courseid , professor name , time period etc.) --> offer gets validated for duplicates (functionality for later maybe?) --> offer gets created

Situation 3 (student wants to find specific offer and send switch-offer request) --> must be logged in --> main page --> can see all currently open offers --> can filter for specific offers --> can click on send trade request button to a specific offer --> request to the offer creator gets send which he can accept

Situation 4 (student wants to look up his switch request for his offer) --> must be logged in --> requests page --> can accept or decline offers --> when declined, requester can see unsuccesful on status page ; when accepted open offer gets hidden on main page --> studienbüro can see the fullfilled switch offers

Situation 5 (Studienbüro) --> has special account with extra page only they can access --> gets list of fullfiled switch offers --> does their thing to make switch happen on their own Software --> clicks on switch made --> this offer gets hidden for Studienbüro too --> the students can see their successfull switches on status page

---

## Target Scope

Our webapp includes following functionality:
- Sign up
- Sign in
- Create new course switch offer
- Search for offers
- Request to accept switch offer
- status page with ones succesful/unsuccesful switches
- insight for the Studienburo where they can see completed switch-matches

Specific UI dummys/prototypes we created:
- https://github.com/FynnKlette/Project-FSWD/blob/main/docs/assets/images/Kursb%C3%B6rseAppSkizze.png
- https://github.com/FynnKlette/Project-FSWD/blob/main/docs/assets/images/Kursb%C3%B6rseAppSkizze_sb.png
