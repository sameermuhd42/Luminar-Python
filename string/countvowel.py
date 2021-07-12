str = input("Enter the string: ")
count = 0
for i in str:
    if i in "aeiou":
        count = count + 1
if count == 0:
    print("No Vowels")
else:
    print(count)

