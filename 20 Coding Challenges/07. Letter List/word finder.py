while True:
    load = input("Do you want to load up a previous file? (y/n): ")
    while load not in ["y", "n"]:
        load = input("Incorrect input! Do you want to load up a previous file? (y/n): ")
    if load == "y":
        file_name= input("Enter your file name which you want to load your words: ")

        try:
            with open(file_name,"r") as f:
                user_data = f.readlines()
            words = []
            for line in user_data:
                line = line.strip().split(" ")
                words += [x.strip(" ,.!?").lower() for x in line]
            break

        except FileNotFoundError:
            print("This file does not exist")

    if load == "n":
        words = [
            "green","controller","potion","robot","burger",
            "paper","spider","grass","skeleton","insurance"
        ]
        break

print("Type in a letter and I will see if any words start with it in a list!")
letter = input().lower().strip()
while not letter.isalpha() or len(letter) != 1:
    letter = input("Incorrect input! please type in a letter: ").lower().strip()

correct = 0
previous = []
for word in words:
    if word[0] == letter and word not in previous:
        print(word)
        previous.append(word)
        correct += 1
if correct == 0:
    print("There's no word beginning with that letter in that list")