list1 = [1, 2, 3]
list2 = [4, 5, 6, 8]
set1 = {5, 6, 8}
set2 = {10, 11, 12}
list1.append(set1)
print(list1)

list1.extend(list2)
print(list1)
