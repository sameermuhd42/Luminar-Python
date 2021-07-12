def missing(A):
    n = len(A)
    total = (n + 1) * (n + 2) / 2
    sum_A = sum(A)
    return total - sum_A

A = [1,2,4,6,3,7,8]
miss = missing(A)
print(miss)