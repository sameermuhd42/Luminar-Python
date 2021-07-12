list1 = [1, 3, 5, 2, "hello", True]
print(list1)
print(type(list1))

list2 = list()
print(list2)

list2.append(5)     # add element
print(list2)

list2.remove(5)
print(list2)

list2.clear()
print(list2)

del list2

list3 = [1, 2, [3, 4]]      # nesting possible
print(list3)

list4 = [1, 2, 10, 3, 7, 4, 8, 9, 5]
print(list4[2])
print(list4.index(10))
list4[0] = 15
print(list4)
print(list4[-1])
print(len(list4))

print(list4[1:5])       # slice
print(list4[1:5:2])     # slice with step value 2

list4.pop()             # removes last element
print(list4)
print(list4[2])
