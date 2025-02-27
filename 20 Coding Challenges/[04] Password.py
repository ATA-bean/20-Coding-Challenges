
def has_specific_character_set(text:str):
    has_lower = False
    has_upper = False
    has_number = False
    has_special_character = False
    
    count = 0
    for letter in text:
        if ord(text[count]) >= 65 and ord(text[count]) <= 90:
            has_lower = True
        elif ord(text[count]) >= 92 and ord(text[count]) <= 112:
            has_upper = True
        elif ord(text[count]) >= 48 and ord(text[count]) <= 57:
            has_number = True
        elif ord(text[count]) == 32:
            pass
        else:
            has_special_character = True
        count += 1
    
    return {"lower":has_lower,"upper":has_upper,"number":has_number,"special":has_special_character}
def check_password():
    correct_format = False
    
    while correct_format == False:
        password  = str(input("Please input a password for your account."))
        character_set = has_specific_character_set(password)
        
        if len(password) >= 8 and character_set["lower"] == True and character_set["upper"] == True:
            correct_format = True
        else:
            print("password did not meet requirements")
    print("Thank you!")
    return password

def password_reinput_match(password,iterations : int):
    
    check_passed = False
    attempts = 3
    while iterations != 0 and attempts != 0:
        check_passed = False
        print("please input your password again")
        user_input = input("")
        
        while user_input != password:
            if user_input == password:
                print("thank you, the password matches")
                iterations -= 1
                print(iterations)
                check_passed = True
            else:
                print("please try again")
                attempts -= 1
            
            if attempts == 0:
                break
    return check_passed
 
user_password = check_password()
password_reinput_match(user_password,2)
