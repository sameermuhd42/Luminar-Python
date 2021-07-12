initial = int(input("Enter the initial value of range: "))
final = int(input("Enter the final value of range: "))
if initial and final > 0:
    while initial <= final:
        if initial % 2 == 0:
            print(initial)
        elif initial % 2 != 0 and initial == final:
            print("No even numbers in the given range")
        initial += 1
else:
    print("Please enter positive integers")