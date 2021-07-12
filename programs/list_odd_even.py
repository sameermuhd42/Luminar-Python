list_no = {1, 2, 3, 4, 5, 6, 7, 8, 9}
list_odd = list()
list_even = list()
for i in list_no:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)
print(list_odd)
print(list_even)
