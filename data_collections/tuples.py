tuple1 = tuple()
print(type(tuple1))

tuple2 = (1, 2, 3, 4, 5)
print(tuple2)
print(max(tuple2))
print(min(tuple2))
print(len(tuple2))

print(tuple2[1])
print(tuple2[-1])
print(tuple2[1:3])
print(tuple2[::-1])     # reverse

# tuple with different data types
tuple3 = ("Hai", 5, 3.4, True)
print(tuple3)
a, b, c, d = tuple3     # tuple unpacking concept
print(a)
print(b)
print(c)
print(d)

# nested tuple
tuple4 = ('mouse', (1, 2, 3), [4, 5, 6])

# tuple with one element, because it considered as int type
# when comma is not used
tuple5 = (25,)
print(tuple5)

tuple6 = ('a', 'p', 'p', 'l', 'e')
print(tuple6.count('p'))
print(tuple6.index('p'))
