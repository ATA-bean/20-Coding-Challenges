#[[item , shop , priority, item_brought? , max_user_price , quantity]]
def ask_for_item():
    
    priorities_index = {"low" : 1,"medium" : 2,"high" : 3}

    item = input("enter the item that you would like to add to the list:")
    shop = input("What shop are you going to get the item from:")
    priority = input("What is the priority of this item, enter high, medium or low:")
    item_brought = input("Have you already brught this item, enter yes or no:")
    max_user_price = float(input("How much are you willing to pay for this item:"))
    quantity = int(input("How many of these items do you need:"))

    priority = priority.lower().strip()
    priority = priorities_index[priority]
    
    item_brought = item_brought.lower().strip()
    item_brought = (item_brought == "yes")

    return [item,shop,priority,item_brought,max_user_price,quantity]

def calculate_estimate_price(shopping_list : list):
    estimated_price = 0
    for items in shopping_list:
        if items[3] == False:
            estimated_price = items[5] * items[4]
    return estimated_price

def main():
    quit_loop = False
    shopping_list = []
    
    count = 0
    while quit_loop == False:
        shopping_list.insert(count,ask_for_item())
        count += 1

        print("enter 'quit' to quit entering items and generate an estimate for the price")
        user_input =input("")
        user_input = user_input.lower().strip()
        if user_input == "quit":
            quit_loop = True
    
    print(calculate_estimate_price(shopping_list))

main()
