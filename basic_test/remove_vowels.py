str1 = input("Enter the string: ")
vowels = "aeiou"
if str1 == "":
    print("Please enter a string!")
else:
    result = ""
    for i in str1:
        if i not in vowels:
            result = result + i
    print(result)
