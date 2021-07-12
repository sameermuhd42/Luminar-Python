bal = 5000
bal_withdraw = int(input("Enter the amount to be withdraw : "))
if bal_withdraw > bal:
    print("Insufficient balance!")
else:
    print("Available balance :", bal - bal_withdraw)
