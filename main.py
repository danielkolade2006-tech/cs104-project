# Sports IQ Challenge
# Daniel Oladejo
# A quiz/questionnaire program built for CS 104 Project 1

# --- Variables ---
score = 0
answer = ""
second_chance_answer = ""
result_message = ""

# --- Welcome message ---
print("Welcome to Sports IQ Challenge!")
print("Are you a Rookie or a Fanatic? Let's find out with some sports trivia.")
print()

# --- Question 1 ---
print("Which sport is played at Wimbledon?")
print("1 - Tennis")
print("2 - Golf")
print("3 - Cricket")
answer = input("Enter 1, 2, or 3: ")

if answer == "1":
    print("Correct! Wimbledon is a Tennis tournament.")
    score += 1
else:
    print("Not quite. The correct answer is Tennis (1).")

print()

# --- Question 2 ---
print("How many players are on the court for one basketball team during play?")
print("1 - 4")
print("2 - 5")
print("3 - 6")
answer = input("Enter 1, 2, or 3: ")

if answer == "2":
    print("Correct! There are 5 players on the court per team.")
    score += 1
else:
    print("Not quite. The correct answer is 5 (2).")

print()

# --- Question 3 ---
print("The Olympic Games are held every four years. Enter yes or no.")
answer = input("Your answer: ")

if answer.lower() == "yes":
    print("Correct! The Olympics are held every four years.")
    score += 1
else:
    print("Not quite. The correct answer is yes.")

print()

# --- Question 4 ---
print("Which country has won the most FIFA World Cups?")
print("1 - Germany")
print("2 - Argentina")
print("3 - Brazil")
answer = input("Enter 1, 2, or 3: ")

if answer == "3":
    print("Correct! Brazil has won the most FIFA World Cups.")
    score += 1
elif answer != "3" and score == 0:
    print("Not quite, but since you haven't scored yet, here's a second chance!")
    print("Second chance — Which country has the most World Cup titles?")
    print("1 - Brazil")
    print("2 - Germany")
    second_chance_answer = input("Enter 1 or 2: ")

    if second_chance_answer == "1":
        print("Correct! Brazil has won the most FIFA World Cups.")
        score += 1
    else:
        print("Not quite. The correct answer is Brazil (1).")
else:
    print("Not quite. The correct answer is Brazil (3).")

print()

# --- Question 5 ---
print("A 'touchdown' is a scoring term used in soccer. Enter yes or no.")
answer = input("Your answer: ")

if answer.lower() == "no":
    print("Correct! Touchdown is a football term, not soccer.")
    score += 1
else:
    print("Not quite. The correct answer is no, touchdown is a football term.")

print()

# --- Final Results ---
print("Here are your results!")
print("Your final score:", score, "out of 5")

if score == 4 or score == 5:
    result_message = "Sports Fanatic! You really know your stuff."
elif score == 2 or score == 3:
    result_message = "Solid Fan! You know a decent amount, but there's more to learn."
else:
    result_message = "Rookie! You're just getting started, but every fan begins somewhere."

print(result_message)
