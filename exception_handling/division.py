# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(num1 / num2)

# Exception handling - solve unexpected errors
# try - exceptional code
# except - solving code
# finally - anything

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    print(num1 / num2)
except Exception as e:
    print("Exception occured", e)
finally:
    print("Inside finally")
