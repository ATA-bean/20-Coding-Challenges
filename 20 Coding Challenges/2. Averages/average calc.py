import ast

try:
    with open("numbers.txt", "r") as f:
        numbers = ast.literal_eval(f.read())
    load = input("Do you want to load up the previous numbers? (y/n): ").strip().lower()
    while load not in ["y","n"]:
        load = input("Incorrect Input! Do you want to load up the previous numbers? (y/n): ").strip().lower()
    if load == "n":
        numbers = []

    else:
        numbers = []
except FileNotFoundError:
    numbers = []


count = 0
while True:
    number = input("Type in the number (type 0 to display averages, or press enter to quit program): ").strip()
    while not number.isdigit() and number != "":
        number = input("Incorrect Input! Type in a number: ").strip()
    if number == "0" or number == "":
        break
    numbers.append(int(number))
    count += 1

if number != "":
    try:
        mode = max(set(numbers), key=numbers.count)

        total = 0
        for number in numbers:
            total += number
        mean = round(total/len(numbers),2)

        sort_numbers = sorted(numbers)
        if len(sort_numbers)%2 == 1:
            median = sort_numbers[len(sort_numbers)//2]
        else:
            median = (sort_numbers[len(sort_numbers)//2] + sort_numbers[(len(sort_numbers)//2)-1]) / 2
    except ValueError or ZeroDivisionError:
        mode = "0"
        median = "0"
        mean = "0"

    print(f"mode: {mode}, mean: {mean}, median: {median}")

save = input("Do you want to save these numbers? (y/n): ").lower().strip()
while save not in ["y", "n"]:
    save = input("Incorrect Input! Do you want to save these numbers? (y/n): ").lower().strip()
if save == "y":
    user_data = numbers
    with open("numbers.txt","w") as f:
        f.write(str(user_data))