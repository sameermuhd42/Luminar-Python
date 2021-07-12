import re

f1 = open("regno", "r")
f2 = open("regcopy", "w")
regex = '[pyPY]'
for i in f1:
    print(i)
    if re.findall(regex, i):
        f2.write(i)
    print(f2.read())
