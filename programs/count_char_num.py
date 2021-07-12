str1 = "malayalam123"
num = "0123456789"
count_char = 0
count_num = 0
for i in str1:
    if i in num:
        count_num = count_num + 1
    else:
        count_char = count_char + 1
print("No. of num: ", count_num)
print("No. of char: ", count_char)