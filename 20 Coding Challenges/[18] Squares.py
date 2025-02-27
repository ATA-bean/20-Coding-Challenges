def print_squares(number_of_squares: int):
    count = 1
    while count < (number_of_squares + 1):
        print(count,"squared is",(count**2))
        count += 1

user = int(input("please enter a number:"))
print_squares(user)