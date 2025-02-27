import os

max_value = int(input("please enter the max bound for the list"))
min_value = int(input("please enter the min bound for the list"))

print("please enter the values for the list, press enter once your done")

user_list = []

while True:
    user_input = input("")

    if user_input == "":
        break
    elif min_value <= int(user_input) <= max_value:
        user_list.append(int(user_input))
    else:
        print("value entered is not within the bounds set")

script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "user_list.txt"

output_path = os.path.join(script_dir, file_name)
text = "list = " + ((str(user_list).replace("[","")).replace("]",""))

with open(output_path,"w") as file:
    file.write(text)
    print('file saved!')