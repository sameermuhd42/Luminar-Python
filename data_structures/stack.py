# Data structures - to store data
# Stack - LIFO (Last In First Out)
# Stack operations - Push and Pop

stack = list()
size = int(input("Enter the size for stack: ")) - 1
top = len(stack)
n1 = 0


def push(n):
    global top, size
    if top <= size:
        stack.append(n)
        print(n, "is pushed into stack")
        top += 1
    else:
        print("Stack Overflow")


def pop():
    global top, size
    if top <= 0:
        print("Stack Underflow")
    else:
        print(stack[top - 1], "is popped from stack")
        stack.pop()
        top -= 1


def display():
    print(stack)


while n1 != 1:
    print("Enter the stack operation to perform")
    print("1. Push \n2. Pop \n3. Display")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter the element to push: "))
        push(num)
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    n1 = int(input("Do yo want to continue? Press 1 for exit"))
