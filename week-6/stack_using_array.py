# Stack using Array
stack = []
MAX = 5
def push():
    if len(stack) == MAX:
        print("Stack Overflow")
    else:
        value = int(input("Enter element: "))
        stack.append(value)
        print("Element pushed successfully.")
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        value = stack.pop()
        print("Popped element:", value)
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])
while True:
    print("\n===== STACK USING ARRAY =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()

    elif choice == 5:
        print("Program ended.")
        break
    else:
        print("Invalid choice.")
