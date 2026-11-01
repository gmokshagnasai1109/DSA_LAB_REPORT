# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter element: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head

                while temp.next is not None:
                    temp = temp.next

                temp.next = new_node

        print("Created Linked List:")
        self.display()

    # Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter element: "))

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        print("After insertion at beginning:")
        self.display()

    # Insert at End
    def insert_end(self):
        data = int(input("Enter element: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

        print("After insertion at end:")
        self.display()

    # Insert at Index
    def insert_at_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter element: "))

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            print("After insertion:")
            self.display()
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp is None:
            print("Index out of range")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        print("After insertion:")
        self.display()

    # Delete by Value
    def delete_by_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("After deletion:")
            self.display()
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print("After deletion:")
                self.display()
                return

            temp = temp.next

        print("Value not found")

    # Delete First Node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next
            print("After deleting first node:")
            self.display()

    # Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            print("After deleting last node:")
            self.display()
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

        print("After deleting last node:")
        self.display()

    # Count Nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program

sll = SinglyLinkedList()

while True:

    print("\n========== SLL MENU ==========")
    print("1. Create Linked List")
    print("2. Insert Beginning")
    print("3. Insert End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display / Traverse")
    print("10. Exit")
    print("==============================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sll.create()

    elif choice == 2:
        sll.insert_beginning()

    elif choice == 3:
        sll.insert_end()

    elif choice == 4:
        sll.insert_at_index()

    elif choice == 5:
        sll.delete_by_value()

    elif choice == 6:
        sll.delete_first()

    elif choice == 7:
        sll.delete_last()

    elif choice == 8:
        sll.count_nodes()

    elif choice == 9:
        sll.display()

    elif choice == 10:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
