import re
def check(data: str) -> bool:

    if len(data) >= 10 and re.search("[a-z]+", data) and re.search("[A-Z]+", data) and re.search("[0-9]+", data):
        print("Password is correct")
        return True
    else:
        print("Password is incorrect")
        return False

check(input("Enter your password: "))