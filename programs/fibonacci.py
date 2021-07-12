terms = int(input("How many terms you want: "))
n1 = 0
n2 = 1
count = 2
if terms <= 0:
    print("Please enter a positive integer")
elif terms == 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
    print(n1, ",", n2, end=", ")
    while count < terms:
        nth = n1 + n2
        print(nth, end=', ')
        n1 = n2
        n2 = nth
        count += 1

# n1 = 0
# n2 = 1
# for i in range(10):
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
