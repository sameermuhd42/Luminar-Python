n = int(input("Enter the value of n: "))
fact = 1
if n > 0:
    for i in range(1, n + 1):
        fact = fact * i
    print("The factorial of", n, "is", fact)
elif n == 0:
    print("The factorial of 0 is 1")
else:
    print("Negative number")
