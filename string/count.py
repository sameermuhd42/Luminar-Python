str = "malayalam"
ch = input("Enter the element: ")
count = 0
for i in str:
    if i in ch:
        count = count + 1
print(ch, "is present", count, "times in", str)
