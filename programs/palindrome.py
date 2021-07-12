# num = int(input("Enter no: "))
# rev = 0
# while num != 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print(rev)

org_str = input("Enter a string: ").lower()
rev_str = org_str[::-1]
if org_str == rev_str:
    print("Palindrome")
else:
    print("Not Palindrome")
