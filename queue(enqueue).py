# Queue implementation using Array/List

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item):
        if len(self.queue) == self.size:
            print("Queue Overflow! Queue is full.")
        else:
            self.queue.append(item)
            print(item, "inserted into the queue.")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow! Queue is empty.")
        else:
            item = self.queue.pop(0)
            print(item, "deleted from the queue.")

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:", self.queue)


# Main program
size = int(input("Enter the size of queue: "))
q = Queue(size)

while True:
    print("\n--- QUEUE MENU ---")
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
