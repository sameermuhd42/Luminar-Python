# Data structures - to store data
# Queue - FIFO (First In First Out)
# Queue operations - Enqueue (insertion) and Dequeue (deletion)

queue = list()
size = int(input("Enter the size for queue: ")) - 1
front = 0
rear = len(queue)
n1 = 0


def enqueue(n):
    global front, rear, size
    if rear <= size:
        queue.insert(rear, n)
        print(n, "is enqueued into queue")
        rear += 1
    else:
        print("Queue is full")


def dequeue():
    global front, rear, size
    if front == rear:
        print("Queue is empty")
    else:
        print(queue[front], "is dequeued from queue")
        queue.pop(front)
        rear -= 1


def display():
    print(queue)


while n1 != 1:
    print("Enter the queue operation to perform")
    print("1. Enqueue \n2. Dequeue \n3. Display")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter the element to enqueue: "))
        enqueue(num)
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    n1 = int(input("Do yo want to continue? Press 1 for exit"))

