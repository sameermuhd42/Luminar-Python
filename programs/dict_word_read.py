# count = dict()
# string = input("Enter the string: ")
# words = string.split(" ")
# for word in words:
#     if word not in count:
#         count.update({word: 1})
#     else:
#         val = int(count[word])
#         val += 1
#         count.update({word: val})
# print(count)


dict1 = dict()
string = input("Enter the string: ")
words = string.split(" ")
for word in words:
    count = words.count(word)
    dict1.update({word: count})
print(dict1)


# def count_frequency(list1):
#     # Creating an empty dictionary
#     freq = dict()
#     for item in list1:
#         if item in freq:
#             freq[item] += 1
#         else:
#             freq[item] = 1
#
#     for key, value in freq.items():
#         print("% d : % d" % (key, value))
#
#
# my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
# count_frequency(my_list)
