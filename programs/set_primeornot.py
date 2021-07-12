set_no = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
set_prime = set()
set_not_prime = set()
for i in set_no:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                set_not_prime.add(i)
                break
        else:
            set_prime.add(i)
print(set_prime)
print(set_not_prime)
