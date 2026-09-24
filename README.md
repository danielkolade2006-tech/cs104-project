# Sports IQ Challenge
> Rookie to Fanatic → Think you know sports? Let's find out.

## Overview
> This program, Rookie to Fanatic, is a knowledge-based quiz that tests users on general sports trivia spanning tennis, basketball, the Olympics, soccer, and the FIFA World Cup. Users are asked a series of multiple-choice and yes/no questions about well-known sports facts. Each time a user answers correctly, their score increases by one point. If a user misses a key question early on, they're given a second-chance nested question to try again before moving on. At the end of the quiz, the program uses the user's final score to determine their sports knowledge level displaying one of three results: "Rookie," "Solid Fan," or "Sports Fanatic" along with an encouraging, tailored message based on how they did.

## Sample Questions and Responses
> 1. Which sport is played at Wimbledon?
a. Tennis
b. Golf
c. Cricket
> 2. How many players are on the court for one basketball team during play?
a. 4
b. 5
c. 6
> 3. The Olympic Games are held every four years. Enter yes or no.
> 4. Which country has won the most FIFA World Cups?
a. Germany
b. Argentina
c. Brazil
> 5. A "touchdown" is a scoring term used in soccer. Enter yes or no.

## Variables
> score (int): tracks the user's total number of correct answers across the quiz. A single variable works here since the final result is based on one cumulative point total, not multiple competing categories.
answer (int or str): stores the user's response to whichever question is currently being asked, compared against the correct option to decide if score increases. Reused for each question rather than having a separate variable per question.
second_chance_answer (int): stores the user's response to the nested retry question, only used if the initial World Cup question (Q4) is answered incorrectly.
result_message (str): stores the final message shown to the user, assigned based on which score range they fall into.

## Conditional Logic Outline
>Conditional statement 1 — related to "Which sport is played at Wimbledon? 1-Tennis 2-Golf 3-Cricket"
if response is 1 (Tennis): display congratulatory message, increment score by 1
else: display incorrect message and explain the correct answer
Conditional statement 2 — related to "How many players are on the court for one basketball team during play? 1-4 2-5 3-6"
if response is 2 (5): display congratulatory message, increment score by 1
else: display incorrect message and explain the correct answer
Conditional statement 3 — related to "The Olympic Games are held every four years. Enter yes or no."
if response is "yes": display congratulatory message, increment score by 1
else: display incorrect message and explain the correct answer
Conditional statement 4 — related to "Which country has won the most FIFA World Cups? 1-Germany 2-Argentina 3-Brazil"
if response is 3 (Brazil): display congratulatory message, increment score by 1
elif response is not 3 AND score is 0 (user hasn't gotten anything right yet, so they get extra help): display a message giving a second chance, then present a nested conditional with only two options (Brazil or Germany)
Conditional statement 5 (nested in statement 4) — related to "Second chance — Which country has the most World Cup titles? 1-Brazil 2-Germany"
if response is 1 (Brazil): display congratulatory message, increment score by 1
else: display incorrect message and explain the correct answer
else: display incorrect message and explain the correct answer (used when the user already has at least 1 point, so no second chance is given)
Conditional statement 6 — related to "A 'touchdown' is a scoring term used in soccer. Enter yes or no."
if response is "no": display congratulatory message, increment score by 1
else: display incorrect message and explain the correct answer
Conditional statement 7 — reveals final results based on the value of score
if score is 4 or 5: display "Sports Fanatic" message, congratulating them on strong sports knowledge
elif score is 2 or 3: display "Solid Fan" message, noting decent knowledge and encouraging them to learn more
else (score is 0 or 1): display "Rookie" message, encouraging them without being discouraging
>


## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]
