# using swapping

# list1 = [1, 2, 10, 3, 7, 4, 8, 9, 5]
# print("Initial list:", list1)
# list_size = len(list1)
# for i in range(list_size):
#     for j in range(i + 1, list_size):
#         if list1[i] > list1[j]:
#             temp = list1[i]
#             list1[i] = list1[j]
#             list1[j] = temp
# print("Sorted list:", list1)


list1 = [1, 2, 10, 3, 7, 4, 8, 9, 5]
new_list = list()
print("Initial list:", list1)
while list1:
    min_value = list1[0]
    for i in list1:
        if i < min_value:
            min_value = i
    new_list.append(min_value)
    list1.remove(min_value)
print("Sorted list: ", new_list)

