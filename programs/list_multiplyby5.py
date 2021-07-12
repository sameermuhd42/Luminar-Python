list1 = [11, 2, 10, 3, 11, 4, 8, 9, 2, 5]
list_size = len(list1)
list_mul = list()
for i in range(list_size):
    list_mul.append(list1[i] * 5)
print(list_mul)


# # List comprehensions are used for creating new lists from other iterables.
# # As list comprehensions return lists, they consist of brackets containing the expression,
# # which is executed for each element along with the for loop to iterate over each element.

list_mul = [i * 5 for i in list1]       # List comprehension
print(list_mul)

list_even = [i for i in range(0, 20) if i % 2 == 0]
print(list_even)

list_8 = [i for i in range(1, 1000) if i % 8 == 0]
print(list_8)
