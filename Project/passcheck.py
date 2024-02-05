import re
def password_check(cur):
    check = 0
    if not len(cur) >= 8:
        print("Password should be atleast 8 char long")
        if not check:
            check = 1
    if not re.search('[A-Z]',cur):
        print("Password must have one Uppercase letter")
        if not check:
            check = 1
    if not re.search('[0-9]',cur):
        print("Password must have a numerical value")
        if not check:
            check = 1
    if not re.search('[!@#$%^&*(),.?":{}|<>]',cur):
        print("Password must have one or more special char")
        if not check:
            check = 1
    return check

cur = input("Create password: ")
if password_check(cur) == 0:
    print("Password is okay")