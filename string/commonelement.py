str = "abc"
str1 = "bcd"
common = ""
for i in str:
    if i in str1:
        common = common + i
if common == "":
    print("No common elements")
else:
    print(common)


# str = "abcde"
# str1 = "bcd"
# notcommon = ""
# for i in str:
#     if i not in str1:
#         notcommon = notcommon + i
# print(notcommon)
