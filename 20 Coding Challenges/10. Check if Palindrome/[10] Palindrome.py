def check_palindrome(input_string: str):
    input_string = input_string.lower()
    reversed_string = "".join(reversed(input_string))
    return reversed_string == input_string

user_input = input("please input a string:")
is_ = "isn't"
if check_palindrome(user_input):
    is_ = "is"
print("The string entered",is_,"a palindrome")