list1 = [5, 8, 2, 10]
index = int(input("Enter the index: "))
try:
    print(list1[index])
except Exception as e:
    print("Exception occured", e)
else:
    print("Found Successfully")
finally:
    print("Inside finally")
