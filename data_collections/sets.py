set1 = {1, 3, 7, 45, 76, 12, 7}
set2 = set((1, 10, 4, 8, 45,24))
print(set1)
print(set2)
print(type(set1))
print(len(set1))

set3 = set()
set3.add("Hello")   # add element
set3.add(True)
set3.add(6)
print(set3)

set3.remove(True)
print(set3)     # delete specific

set3.clear()    # delete all
print(set3)

del set3        # delete set

set4 = {1, 2, {3, 4}}
print(set4)     # nesting not possible
