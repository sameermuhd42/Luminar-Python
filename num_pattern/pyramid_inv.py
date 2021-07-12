n = int(input("Enter the no. of rows: "))
k = n
for i in range(n, 0, -1):
    for j in range(0, k):
        print(end=" ")
    k += 1
    for l in range(0, i - 1):
        print("* ", end=" ")
    print("\r")
