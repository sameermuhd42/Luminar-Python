from functools import reduce

# map() method
# syntax: map(function, iterables)

list1 = [1, 2, 3, 4, 5, 6, 7]

products = [
    {'item_name': 'Boost', 'price': 250, 'stock': 30},
    {'item_name': 'Horlicks', 'price': 230, 'stock': 50},
    {'item_name': 'Complan', 'price': 260, 'stock': 0}
]

# def square(num):
#     return num ** 2

# sq = list(map(square, list1))
sq = list(map(lambda num: num ** 2, list1))
print(sq)

names = list(map(lambda product: product['item_name'], products))
print(names)

# ---------------------------------------------------------------
# filter() method
# syntax: filter(function, iterables)

even = list(filter(lambda num: num % 2 == 0, list1))
print(even)
odd = list(filter(lambda num: num % 2 == 1, list1))
print(odd)

out_of_stock = list(filter(lambda product: product['stock'] == 0, products))
print(out_of_stock)

price_below_250 = list(filter(lambda product: product['price'] <= 250, products))
items = list(map(lambda product: product['item_name'], price_below_250))
# print(price_below_250)
# print(items)
print("Items that price below 250:")
for item in items:
    print(item)

#
# num1 = 10
# result = '+ve' if num1 > 0 else '-ve'


list2 = [2, 3, 4, 5, 8, 10, 7]
res = list(map(lambda num: num + 1 if num > 5 else num - 1 if num < 5 else num, list2))
print(res)

nums = range(2, 100)
for i in range(2, 10):
    nums = list(filter(lambda x: x == i or x % i, nums))
print(nums)

# ---------------------------------------------------------------
# reduce() method - to return single value, for int only
# syntax: reduce(function, iterables)

total = reduce(lambda num1, num2: num1 + num2, list2)
print(total)
largest = reduce(lambda num1, num2: num1 if num1 > num2 else num2, list2)
print(largest)

prices = list(map(lambda product: product['price'], products))
print(prices)
high_price = reduce(lambda price1, price2: price1 if price1 > price2 else price2, prices)
print(high_price)

# Instead of this
price_max = max(list(map(lambda product: product['price'], products)))
print(price_max)
