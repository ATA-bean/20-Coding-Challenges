import ast
import random
grades = {
    10: "S",
    9: "A", 8: "A",
    7: "B", 6: "B",
    5: "C", 4: "C",
    3: "D", 2: "D",
    1: "F", 0: "F"
}
try:
    with open("quiz questions","r") as f:
        questions = ast.literal_eval(f.read())
    correct = 0
    for count in range(10):
        choice = random.choice(questions)
        questions.remove(choice)
        question = choice[0]
        answer = choice[1]
        print(question)
        user = input().upper().strip()
        if user == answer:
            print("You got it correct!")
            correct += 1
        else:
            print(f"Uh oh, you got it wrong...\nThe answer is {answer}")

    print(f"You got {correct} correct!\nYour grade is {grades[correct]}")

except FileNotFoundError:
    print("Can't find any questions. Sorry!")

