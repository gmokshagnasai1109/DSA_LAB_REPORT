class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# INSERT
def insert(root, x):
    if root is None:
        return Node(x), True

    if x < root.data:
        root.left, inserted = insert(root.left, x)
    elif x > root.data:
        root.right, inserted = insert(root.right, x)
    else:
        print("Duplicate value is not allowed.")
        inserted = False

    return root, inserted

# INORDER TRAVERSAL
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

# PREORDER TRAVERSAL
def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

# POSTORDER TRAVERSAL
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

# FIND MINIMUM
def find_min(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root


# FIND MAXIMUM
def find_max(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root


# SEARCH
def search(root, data):
    if root is None:
        return None

    if data < root.data:
        return search(root.left, data)
    elif data > root.data:
        return search(root.right, data)
    else:
        return root


# COUNT TOTAL NODES
def count_nodes(root):
    if root is None:
        return 0

    return (count_nodes(root.left)
            + count_nodes(root.right) + 1)


# COUNT LEAF NODES
def count_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaves(root.left) + count_leaves(root.right)


# COUNT INTERNAL NODES
def count_internal(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 0

    return (count_internal(root.left)
            + count_internal(root.right) + 1)


# HEIGHT OF BST
def height(root):
    if root is None:
        return -1

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1

# DELETE
def delete(root, x):
    if root is None:
        return None, False

    if x < root.data:
        root.left, deleted = delete(root.left, x)

    elif x > root.data:
        root.right, deleted = delete(root.right, x)

    else:
        # Case 1: No children
        if root.left is None and root.right is None:
            return None, True

        # Case 2: Only right child
        elif root.left is None:
            return root.right, True

        # Case 3: Only left child
        elif root.right is None:
            return root.left, True

        # Case 4: Two children
        else:
            successor = find_min(root.right)
            root.data = successor.data
            root.right, _ = delete(root.right, successor.data)
            return root, True

    return root, deleted


# PRINT A PARTICULAR LEVEL
def print_level(root, level):
    if root is None:
        return

    if level == 0:
        print(root.data, end=" ")
    else:
        print_level(root.left, level - 1)
        print_level(root.right, level - 1)


# LEVEL ORDER TRAVERSAL
def level_order(root):
    if root is None:
        return

    h = height(root)

    for level in range(h + 1):
        print_level(root, level)


# MAIN PROGRAM
root = None

while True:
    print("\n\n******** BINARY SEARCH TREE ********")
    print("1. INSERT")
    print("2. PREORDER TRAVERSAL")
    print("3. INORDER TRAVERSAL")
    print("4. POSTORDER TRAVERSAL")
    print("5. FIND MINIMUM")
    print("6. FIND MAXIMUM")
    print("7. SEARCH")
    print("8. DELETE")
    print("9. COUNT NODES")
    print("10. COUNT LEAVES")
    print("11. COUNT INTERNAL NODES")
    print("12. HEIGHT")
    print("13. LEVEL ORDER TRAVERSAL")
    print("14. EXIT")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        try:
            data = int(input("Enter the data to be inserted: "))
            root, inserted = insert(root, data)

            if inserted:
                print("Element inserted successfully.")
        except ValueError:
            print("Please enter an integer.")

    elif choice == 2:
        if root is None:
            print("Tree is empty.")
        else:
            print("Preorder Traversal:", end=" ")
            preorder(root)
            print()

    elif choice == 3:
        if root is None:
            print("Tree is empty.")
        else:
            print("Inorder Traversal:", end=" ")
            inorder(root)
            print()

    elif choice == 4:
        if root is None:
            print("Tree is empty.")
        else:
            print("Postorder Traversal:", end=" ")
            postorder(root)
            print()

    elif choice == 5:
        node = find_min(root)

        if node is None:
            print("Tree is empty.")
        else:
            print("Minimum element:", node.data)

    elif choice == 6:
        node = find_max(root)

        if node is None:
            print("Tree is empty.")
        else:
            print("Maximum element:", node.data)

    elif choice == 7:
        try:
            data = int(input("Enter the data to be searched: "))
            node = search(root, data)

            if node is None:
                print("Element", data, "is not found.")
            else:
                print("Element", data, "is found.")
        except ValueError:
            print("Please enter an integer.")

    elif choice == 8:
        try:
            data = int(input("Enter the data to be deleted: "))
            root, deleted = delete(root, data)

            if deleted:
                print("Element deleted successfully.")
            else:
                print("Element not found.")
        except ValueError:
            print("Please enter an integer.")

    elif choice == 9:
        print("Number of nodes:", count_nodes(root))

    elif choice == 10:
        print("Number of leaf nodes:", count_leaves(root))

    elif choice == 11:
        print("Number of internal nodes:", count_internal(root))

    elif choice == 12:
        print("Height of BST:", height(root))

    elif choice == 13:
        if root is None:
            print("Tree is empty.")
        else:
            print("Level Order Traversal:", end=" ")
            level_order(root)
            print()

    elif choice == 14:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")
