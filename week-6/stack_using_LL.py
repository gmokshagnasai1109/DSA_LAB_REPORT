# Stack using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    # Push operation
    def push(self):
        value = int(input("Enter element: "))
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print("Element pushed successfully.")
    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            value = self.top.data
            self.top = self.top.next
            print("Popped element:", value)
    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)
    # Display operation
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements:")
            while temp is not None:
                print(temp.data)
                temp = temp.next
                
# Main Program
stack = Stack()
while True:
    print("\n===== STACK USING LINKED LIST =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        stack.push()
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.display()
    elif choice == 5:
        print("Program ended.")
        break
    else:
        print("Invalid choice.")
