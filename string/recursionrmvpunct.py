def inp():
    str = input("Enter the string: ")
    punctuations = '''",./;:><?'()*&#@!%=+-_'''
    if str == "":
        print("Please provide a string!")
        inp()
    else:
        result = ""
        for i in str:
            if i not in punctuations:
                result = result + i
        print(result)


inp()
