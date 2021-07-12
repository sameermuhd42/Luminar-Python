string = input("Enter string: ")
dict1 = {}
for i in string:
    if i not in dict1:
        dict1.update({i: 1})
        print(dict1)
    else:
        print("First recursive element:", i)
        break
