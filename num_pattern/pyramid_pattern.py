n = int(input("Enter the no. of rows: "))
k = n
for i in range(0, n):
    for j in range(0, k):
        print("* ", end="")
    k -= 1
    for l in range(0, i + 1):
        print(end=" ")
    print("\r")

# n = int(input("Enter the no. of rows: "))
# for i in range(1, n):
#     print(" " * (n - i), end=" ")
#     for j in range(0, i):
#         print("*", end=" ")
#     print()
