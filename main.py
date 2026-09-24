# Sports IQ Challenge
# Daniel OLadejo 
# A quiz/questionnaire program built for CS 104 Project 

# TODO: Define your variables here.
# --- Variables ---
score = 0
answer = ""
second_chance_answer = ""
result_message = ""

# TODO: Print a welcome message introducing your program.
print("Welcome to Sports IQ Challenge!")
print("Are you a Rookie or a Fanatic? Let's find out with some sports trivia.")
print()

# TODO: Write your questions and conditional logic here.
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
# Follow the outline you planned in your README.

# TODO: Display the final results to the user.
