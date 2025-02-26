import ast

try:
    with open("Name Lists.txt", "r") as f:
        user_data = ast.literal_eval(f.read())
    print(user_data)
    print(f"Loading user data..")

    load = input("Do you want to load a previous list? (y/n): ").lower().strip()
    while load not in ["y", "n"]:
        load = input("Incorrect Input! Do you want to load a previous list? (y/n): ").lower().strip()

    while load == "y":
        try:
            name_list = user_data[int(input("Which name list do you want to load? (0/1/2/3...): "))]
            break
        except ValueError:
            print("Please type in a number!")
        except IndexError:
            print("Index out of range!")
    else:
        name_list = input("Enter the names with a space in between them: ").lower().strip().split(" ")

except FileNotFoundError:
    print("creating new file... ")
    user_data = []
    name_list = input("Enter the names with a space in between them: ").lower().strip().split(" ")
    load = "n"



print("Which iteration do you want to print out? (type 'no' if you want to stop)")
iteration = input("(normal/reversed/item/slice/remove): ").lower().strip()

while iteration != "no":

    while iteration not in ["normal","reversed","item","slice","remove","no"]:
        iteration = input("Incorrect input! (normal/reversed/item/slice/remove): ").lower().strip()

    if iteration == "normal":
        print(name_list)

    if iteration == "reversed":
        print(list(reversed(name_list)))

    elif iteration == "item":
        while True:
            try:
                item = int(input("Which position do you want to print out? "))
                print(name_list[item])
                break
            except ValueError:
                print("Incorrect input! Please type in an integer")
            except IndexError:
                print("This position is outside the index")

    elif iteration == "slice":
        while True:
            try:
                start = int(input("Where do you want to start? "))
                end = int(input("Where do you want to end? "))
                step = int(input("How many steps do you want skip? "))+1
                print(name_list[start:end:step])
                break
            except ValueError:
                print("Incorrect input! Please type in an integer.")

    elif iteration == "remove":
        item = input("What item do you want to remove? ").strip().lower()
        while item not in name_list:
            item = input("Please input an actual item: ").strip().lower()
        new_list = (name_list.copy())
        new_list.remove(item)
        print(new_list)

    print("Which iteration do you want to print out? (type 'no' if you want to stop)")
    iteration = input("(normal/reversed/item/slice/remove): ").lower().strip()

if load == "n":
    save = input("Do you want to save these names? (y/n): ").lower().strip()
    if save == "y":
        user_data.append(name_list)
        print(user_data)
        with open("Name Lists.txt","w") as f:
            f.write(str(user_data))