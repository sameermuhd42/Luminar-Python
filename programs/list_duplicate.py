list1 = [11, 2, 10, 3, 11, 4, 8, 9, 5, 2, 5]
list_size = len(list1)
list2 = list()
for i in range(list_size):
    k = i + 1
    for j in range(k, list_size):
        if list1[i] == list1[j]:
            if list1[i] not in list2:
                print(list1[i])
