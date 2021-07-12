set_no = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_odd = set()
set_even = set()
for i in set_no:
    if i % 2 == 0:
        set_even.add(i)
    else:
        set_odd.add(i)
print(set_odd)
print(set_even)
