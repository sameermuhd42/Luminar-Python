str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
not_com = ""
rev_str = ""
for i in str1:
    if i not in str2:
        not_com = not_com + i
# print(not_com[::-1])
for j in not_com:
    rev_str = j + rev_str
print(rev_str)
