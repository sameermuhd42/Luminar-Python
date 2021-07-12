start = int(input("Enter the initial value of range: "))
end = int(input("Enter the final value of range: "))
if start and end > 0:
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)
        elif num % 2 != 0 and start == end:
            print("No even numbers in the given range")
else:
    print("Please enter positive integers")
