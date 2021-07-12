lst = [3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
max1 = lst[0]
lst.sort()
n = len(lst)
for i in range(2, n):
    if lst[i] > max1:
        max1 = lst[i]
        break
print("Second largest number is:", max1)
