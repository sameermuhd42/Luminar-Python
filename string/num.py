str1 = input("skywalkglobalpvt")
str2 = ""
numbers = [4, 7, 10]
for i in range(1, 10):
    inputnum = input("Enter the number")
    num = int(inputnum)

    if num not in numbers:
        length = len(str1)
        for j in range(1, length, 2):
            str2 = str2 + j
print(str2)



