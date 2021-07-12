import re

f1 = open("veh_reg", "r")
f2 = open("veh_regcopy", "w")
regex = '(^[K][L]\d{2}\w{1,2}\d{4})'
lines = f1.readlines()
for i in lines:
    print(i)
    if re.fullmatch(regex, i):
        f2.write(i)

