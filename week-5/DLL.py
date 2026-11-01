# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
                new_node.prev = temp

        print("Created Doubly Linked List:")
        self.display()

    # Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter element: "))

        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

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
            new_node.prev = temp
        print("After insertion at end:")
        self.display()

    # Insert at Index
    def insert_at_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter element: "))
        if index < 0:
            print("Invalid index")
            return

        # Insert at beginning
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
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
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        print("After insertion:")
        self.display()

    # Delete by Value
    def delete_by_value(self):
        value = int(input("Enter value to delete: "))
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp is not None:
            if temp.data == value:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                print("After deletion:")
                self.display()
                return
            temp = temp.next
        print("Value not found")

    # Delete First Node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        print("After deleting first node:")
        self.display()

    # Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        if temp.prev is None:
            self.head = None
        else:
            temp.prev.next = None
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
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main Program
dll = DoublyLinkedList()
while True:
    print("\n========== DLL MENU ==========")
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
        dll.create()

    elif choice == 2:
        dll.insert_beginning()

    elif choice == 3:
        dll.insert_end()

    elif choice == 4:
        dll.insert_at_index()

    elif choice == 5:
        dll.delete_by_value()

    elif choice == 6:
        dll.delete_first()

    elif choice == 7:
        dll.delete_last()

    elif choice == 8:
        dll.count_nodes()

    elif choice == 9:
        dll.display()

    elif choice == 10:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
