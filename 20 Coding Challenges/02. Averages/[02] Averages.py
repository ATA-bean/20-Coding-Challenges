import os
def input_numbers():
    list_of_numbers = []
    quit_input = False
    quit_program = False
    
    print("Press enter to calculate the average or type 'quit' to stop the program instead of a number")
    
    count = 0
    while quit_input == False:
        user_input = input("Input a number:")
        if user_input == '':
            quit_input = True
        elif user_input == 'quit':
            quit_input = True
            quit_program = True
        else:
            list_of_numbers.insert(count,int(user_input))
        count += 1
    
    if quit_program == True:
        return None
    else:
        return list_of_numbers

def calculate_mean(numbers: list):
    total = 0
    count = 0
    for letters in numbers:
        total += numbers[count]
        count += 1
    output = total/(len(numbers))
    return output
def calculate_mode(numbers: list):
    output = 0
    count = 0
    for letters in numbers:
        if numbers.count(numbers[count]) > numbers.count(numbers[count-1]):
            output = numbers[count]
        count += 1
    return output
def calculate_median(numbers: list):
    length = len(numbers)
    numbers = sorted(numbers)
    if length % 2 == 0:
        p1 = (numbers[int(length/2) - 1])
        p2 = (numbers[int((length/2))])
        output = calculate_mean([p1,p2])
        return output
    else:
        output = (numbers[int((length)/2)])
        return output

def save_file(numbers: list):
    save = input("Would you like to save your string of numbers as a txt document. accept 'yes' or 'no'")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if save == 'yes':
        text = "numbers = {" + str(numbers) + "}"
        file_name = input("what would you like to call the file") + ".txt"
        output_path = os.path.join(script_dir, file_name)
        
        with open(output_path,"w") as file:
            file.write(text)
            print('file saved!')


def averages_calculator():
    user_input = input_numbers()
    if user_input != None:
        print("The mean is",calculate_mean(user_input))
        print("The mode is",calculate_mode(user_input))
        print("The median is",calculate_median(user_input))
        save_file(user_input)
averages_calculator()