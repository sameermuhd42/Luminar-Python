# n = int(input("Enter thr no. of rows: "))
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("\r")

# n = int(input("Enter thr no. of rows: "))
# for i in range(n + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("* ", end="")
#     print("\r")

# n = 10
# for i in range(n + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("* ", end="")
#     print("\r")
# for k in range(0, n - 1, 1):
#     for l in range(0, k + 1):
#         print("* ", end="")
#     print("\r")

# n = 10
# for i in range(n + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("* ", end="")
#     for k in range(i - 1, n):
#         print(" ", end=" ")
#     for l in range(i - 1, n):
#         print(" ", end=" ")
#     for m in range(0, i - 1):
#         print("* ", end="")
#     print("\r")
# for o in range(0, n - 1, 1):
#     for p in range(0, o + 1):
#         print("* ", end="")
#     for q in range(o, n - 1):
#         print(" ", end=" ")
#     for r in range(o, n - 1):
#         print(" ", end=" ")
#     for s in range(-1, o):
#         print("* ", end="")
#     print("\r")

n=10
for i in range(n+1, 0, -1):
    for j in range(0, i-1):
        print("* ", end="")
    for k in range(i-1, n):
        print(" ", end=" ")
    for l in range(i-1, n):
        print(" ", end=" ")
    for m in range(0, i-1):
        print("* ", end="")
    print("\r")
for o in range(0, n-1, 1):
    for p in range(0, o+1):
        print("* ", end="")
    for q in range(o, n-1):
        print(" ", end=" ")
    for r in range(o, n-1):
        print(" ", end=" ")
    for s in range(-1, o):
        print("* ", end="")
    print("\r")