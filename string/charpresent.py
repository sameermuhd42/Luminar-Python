str = "Luminar"
ch = input("Enter the character to search: ")
for i in str:
    if ch in str:
        print(ch, "is present")
        break
else:
    print(ch, "is not present")
