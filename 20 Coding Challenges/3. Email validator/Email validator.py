import time


def check_email(email):
    local_part = email.split("@")[0] if "@" in email else ""
    domain_part = email.split("@")[1] if "@" in email else ""

    if " " in email:
        print("You cannot have spaces in your email")
    elif "@" not in email:
        print("You need an @ symbol")
    elif "." not in domain_part:
        print("You need a dot after the @ symbol")
    elif email.index("@") > email.index("."):
        print("You need the dot to be after the @ symbol")
    elif len(local_part) > 12:
        print("The first section of your email is too long")
    elif len(local_part) < 5:
        print("The first section of your email is too short")
    elif len(domain_part) > 17:
        print("The last section of your email is too long")
    elif len(domain_part) < 6:
        print("The last section of your email is too short")
    else:
        return True


#Loading file
try:
    with open("Emails.txt", "r") as f:
        user_data = f.readlines()
    print(f"Loading user data..")
    load = input("Do you want to check your emails in the 'Emails.txt' file? (y/n): ").strip().lower()
    while load not in ["y", "n"]:
        load = input("Incorrect input! do you want to use the 'Emails.txt' file? (y/n): ").strip().lower()
    # Checking emails
    if load == "y":
        for user_email in user_data:
            print(f"Email chosen: {user_email.strip()}")
            valid_email = check_email(user_email.strip())
            if valid_email:
                print("This email is perfect!")
            time.sleep(2)

except FileNotFoundError:
    print("creating new file... ")
    user_data = "Input your emails here, each on different lines (delete this line aswell)"
    with open("Emails.txt", "w") as f:
        f.write(user_data + "\n")
    load = "n"

if load == "n":
    valid = False
    while not valid:
        user_email = input("Enter an email: ").strip()
        valid = check_email(user_email)
    print("This email is perfect!")