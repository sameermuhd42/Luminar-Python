str = input("Enter the string: ")
if str == "":
    print("Please enter a string!")
else:
    result = ""
    for i in str:
        if i not in ",./;:><?()*&#@!%=+-_":
            result = result + i
    print(result)
