start = int(input("Enter the initial value of range: "))
end = int(input("Enter the final value of range: "))
s = 0
if start and end > 0:
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                s += i
    print("Sum of prime numbers between", start, "and", end, "are:", s)

