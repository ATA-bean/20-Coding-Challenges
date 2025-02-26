import random

def calculating_change(coins, change_needed):
    output = ""
    for coin in coins:
        while coins.get(coin) <= change_needed:
            change_needed -= coins.get(coin)
            output += coin + " "
    output = output.removesuffix(", ")
    print(f"change: {output}")


british_coins = {"£50":50, "£20":20, "£10":10, "£5":5, "£2":2, "£1":1,
             "50p":0.5,"20p":0.2,"10p":0.1,"5p":0.05,"2p":0.02,"1p":0.01}
american_coins = {"$100":100,"$20":20,"$10":10,"$5":5,"$1":1,
                      "50¢":0.5,"25¢":0.25,"10¢":0.1,"5¢":0.05,"1¢":0.01}

choice = input("Do you want to auto test this program? (y/n): ")
if choice == "y":
    cost = round(random.uniform(0,2), 2)
    print(f"Cost = £{cost} ")
    pay = round(random.uniform(0,200), 2)
    print(f"Payed = £{pay}")
else:
    cost = 0
    pay = -1
    while True:
        try:
            cost = float(input("Please enter the cost in pounds: ").strip(" £"))
            cost = round(cost, 2)
            pay = float(input("Please enter the money payed in pounds: ").strip(" £"))
            pay = round(pay, 2)
            if pay >= cost:
                break
            else:
                print("You haven't payed the correct price!")
        except ValueError:
            print("Incorrect Input! Enter a float")

if cost == pay:
    print("No need for change!")
else:
    change = pay - cost
    calculating_change(british_coins,change)
    calculating_change(american_coins,change)
    if choice == "y":
        print(f"{cost} + {change} = {pay}")


