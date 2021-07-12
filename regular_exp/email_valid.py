import re
regex = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
email = input("Enter the email id: ")
if re.fullmatch(regex, email):
    print("Valid Email")
else:
    print("Invalid Email")
