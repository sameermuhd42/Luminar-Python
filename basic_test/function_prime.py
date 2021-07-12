def prime(limit):
    limit = 10
    sum1 = 0
    for num in range(2, limit + 1):
        i = 2
        for i in range(2, num):
            if int(num % i) == 0:
                i = num
                break
        if i is not num:
            sum1 += num
    return sum1


n = 50
print(prime(n))
