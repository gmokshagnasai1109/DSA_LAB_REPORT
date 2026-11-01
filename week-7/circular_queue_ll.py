# Circular Queue implementation using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, item):
        new_node = Node(item)
        # Queue is empty
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node
        print(item, "inserted into the queue.")
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow! Queue is empty.")
            return
        item = self.front.data
        # Only one node
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        print(item, "deleted from the queue.")
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Front element:", self.front.data)
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        temp = self.front
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:
                break

        print()


q = CircularQueue()

while True:
    print("\n--- CIRCULAR QUEUE USING LINKED LIST ---")
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
