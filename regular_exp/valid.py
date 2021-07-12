import re

# pat = '\w*'
# s = 'hello'
# match = re.fullmatch(pat, s)
# print(match)
# if match is not None:
#     print("Valid")
# else:
#     print("Not valid")

# pat = '\d{2}[k][g]'
# s = '56kg'
# match = re.fullmatch(pat, s)
# print(match)
# if match is not None:
#     print("Valid")
# else:
#     print("Not valid")

# pat = '[a-zA-Z]+\d{1}$'
# s = 'Abc6'
# match = re.fullmatch(pat, s)
# print(match)
# if match is not None:
#     print("Valid")
# else:
#     print("Not valid")

# pat = '(^a[\w\W\d]*b{1}$)'
# s = 'aaa,d67bb'
# match = re.fullmatch(pat, s)
# print(match)
# if match is not None:
#     print("Valid")
# else:
#     print("Not valid")

# pat = '[\D]{8,15}'
# s = 'aBccdefZfg'
# match = re.fullmatch(pat, s)
# print(match)
# if match is not None:
#     print("Valid")
# else:
#     print("Not valid")

pat = '(^[A-Z]{1}[a-z\d\W]+)'
s = 'Abc6>'
match = re.fullmatch(pat, s)
print(match)
if match is not None:
    print("Valid")
else:
    print("Not valid")
