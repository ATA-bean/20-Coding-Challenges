import random
import ast


def ask_for_data(user_data, guesses):
    print("NEW HIGH SCORE!")
    for data in user_data:
        if data["mode"] == mode:
            data["name"] = input("Input your name please: ").title().strip()
            while not data["name"].isalpha():
                data["name"] = input("Please input a suitable name: ").title().strip()
            data["age"] = input("Input your age please: ")
            while not data["age"].isdigit():
                data["age"] = input("Input your age please: ")
            data["high score"] = str(guesses)
            with open("High score.txt", "w") as f:
                f.write(str(user_data))

#Loading highscores
try:
    with open("High score.txt", "r") as f:
        user_data = ast.literal_eval(f.read())
    print(f"Loading user data..")
except FileNotFoundError:
    print("creating new file... ")
    user_data = [
        {"mode": "easy"},
        {"mode": "medium"},
        {"mode": "hard"}
    ]
#Displaying highscores
print("===========HIGH SCORES============")
for data in user_data:
    try:
        print(f"{data['mode'].upper()}: {data['name']} ({data['age']}) - {data['high score']} tries")
    except KeyError:
        print(f"{data["mode"].upper()}: No highscore yet")
#Deciding mode
print("==============GAME================")
mode = input("EASY/MEDIUM/HARD MODE: ").lower().strip()
while mode not in ['easy','medium','hard']:
    mode = input("EASY/MEDIUM/HARD MODE: ").lower().strip()
if mode == "hard":
    length = 5
    random_number = str(random.randint(10000, 99999))
else:
    length = 4
    random_number = str(random.randint(1000, 9999))
#Running game
guesses = 0
user_guess = "0000"
while user_guess != random_number:
    #getting user's guess
    user_guess = input(f"Guess the {length} digit number: ")
    while not user_guess.isdigit() or len(user_guess) != length:
        user_guess = input("Please try again: ")
    #checking if guess is correct
    correct = 0
    for count in range(length):
        if random_number[count] == user_guess[count]:
            if mode == "easy":
                print(f"you got position {count + 1} correct!")
            correct += 1
    #easier readability
    if mode != "easy" or correct == 0:
        print(f"You got {correct} correct!")
    guesses += 1

print("============YOU WIN!=============")
print(f"It took you {guesses} tries!")
#storing highscores
for data in user_data:
    if data["mode"] == mode:
        try:
            previous_score = int(data["high score"])
            if guesses < previous_score:
                ask_for_data(user_data, guesses)
        except KeyError:
            ask_for_data(user_data, guesses)
