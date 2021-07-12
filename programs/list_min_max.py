list1 = [11, 2, 10, 3, 7, 4, 8, 9, 5]
min_value = max_value = list1[0]
for i in list1:
    if i < min_value:
        min_value = i
    elif i > max_value:
        max_value = i
print("Min: ", min_value)
print("Max: ", max_value)
