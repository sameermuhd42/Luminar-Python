f1 = open("new", "r")
dict1 = dict()
string = f1.read()
words = string.split(" ")
for i in words:
    count = words.count(i)
    dict1.update({i: count})
print(dict1)
