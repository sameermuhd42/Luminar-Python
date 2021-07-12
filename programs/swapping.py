# using temp variable
num1 = 10
num2 = 20
print("Value in mum1 before swapping is ", num1)
print("Value in mum2 before swapping is ", num2)
temp = num1
num1 = num2
num2 = temp
print("Value in mum1 after swapping is ", num1)
print("Value in mum2 after swapping is ", num2)

# second approach using assignment concept
num1 = 10
num2 = 20
print("Value in mum1 before swapping is ", num1)
print("Value in mum2 before swapping is ", num2)
(num1, num2) = (num2, num1)
print("Value in mum1 after swapping is ", num1)
print("Value in mum2 after swapping is ", num2)

# third approach
num1 = 10
num2 = 20
print("Value in mum1 before swapping is ", num1)
print("Value in mum2 before swapping is ", num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("Value in mum1 after swapping is ", num1)
print("Value in mum2 after swapping is ", num2)
