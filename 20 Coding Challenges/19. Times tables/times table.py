number = (input("Input the number you want to use for the time table: "))
while not number.isdigit:
    number = (input("Incorrect input! Please input a number: "))

for count in range(1,13):
    product = count * int(number)
    print(f"{count} * {number} = {product}")
