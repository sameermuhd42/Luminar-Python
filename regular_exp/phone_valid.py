import re

# pat = '([\d]{10})'
# phone = input("Enter the phone number: ")
# match = re.fullmatch(pat, phone)
# print(match)
# if match is not None:
#     print("Valid number")
# else:
#     print("Invalid number")

pat = '(^[+][9][1]+[\d]{10})'
phone = '+919995492782'
match = re.fullmatch(pat, phone)
print(match)
if match is not None:
    print("Valid number")
else:
    print("Invalid number")
