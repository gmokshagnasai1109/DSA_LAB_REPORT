# Circular Queue implementation using Array
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    def enqueue(self, item):
        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow! Queue is full.")
            return
        # First element
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(item, "inserted into the queue.")
    def dequeue(self):
        # Check if queue is empty
        if self.front == -1:
            print("Queue Underflow! Queue is empty.")
            return
        item = self.queue[self.front]
        self.queue[self.front] = None
        # If only one element is present
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(item, "deleted from the queue.")
    def peek(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[self.front])
    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
size = int(input("Enter the size of circular queue: "))
q = CircularQueue(size)
while True:
    print("\n--- CIRCULAR QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter element to enqueue: "))
        q.enqueue(item)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.peek()
    elif choice == 4:
        q.display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice! Please try again.")
