def bsearch(list1, x):
    low = 0
    high = len(list1) - 1
    mid = 0
    list1.sort()
    while low <= high:
        mid = (high + low) // 2
        if list1[mid] < x:
            low = mid + 1
        elif list1[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


list2 = [8, 45, 12, 5, 22, 10, 3, 31]
n = int(input("Enter the element: "))
result = bsearch(list2, n)
if result != -1:
    print("Element is present")
else:
    print("Element is not present")
