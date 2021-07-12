init = int(input("Enter the initial range: "))
final = int(input("Enter the final range: "))
r = 5
for i in range(init, final + 1):
    if i % 2 == 0:
        for j in range(r, 0, -1):
            for k in range(0, j):
                print(i, end=" ")
            print("\r")
    else:
        for l in range(r):
            for m in range(0, l + 1):
                print(i, end=" ")
            print("\r")




