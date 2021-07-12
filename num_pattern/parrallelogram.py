n = int(input("Enter the no. of rows: "))
k = n
for i in range(0, n):
    for j in range(0, k - n):
        print(end=" ")
    k += 1
    for l in range(0, n):
        print("* ", end="")
    print("\r")


# n = int(input("Enter the no. of rows: "))
# k = n
# for i in range(0, n):
#     for j in range(0, k):
#         print(end=" ")
#     k -= 1
#     for l in range(0, n):
#         print("* ", end="")
#     print("\r")
