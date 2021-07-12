import re

pat = '(^[K][L]\d{2}\w{1,2}\d{4})'
reg_no = 'KL07CA3333'
match = re.fullmatch(pat, reg_no)
print(match)
if match is not None:
    print("Valid number")
else:
    print("Invalid number")
