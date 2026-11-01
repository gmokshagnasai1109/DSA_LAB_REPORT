class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 
        self.height = 1 
class AVLTree: 
    def height(self, root): 
        if root is None: 
            return 0 
        return root.height 
    def balance(self, root): 
        if root is None: 
            return 0 
        return self.height(root.left) - self.height(root.right) 
    def right_rotate(self, y): 
        x = y.left 
        t = x.right 
        x.right = y 
        y.left = t 
        y.height = 1 + max(self.height(y.left), self.height(y.right)) 
        x.height = 1 + max(self.height(x.left), self.height(x.right)) 
        return x 
    def left_rotate(self, x): 
        y = x.right 
        t = y.left 
        y.left = x 
        x.right = t 
        x.height = 1 + max(self.height(x.left), self.height(x.right)) 
        y.height = 1 + max(self.height(y.left), self.height(y.right)) 
        return y 
    def insert(self, root, data): 
        if root is None: 
            return Node(data) 
        if data < root.data: 
            root.left = self.insert(root.left, data) 
        elif data > root.data: 
            root.right = self.insert(root.right, data) 
        else: 
            return root 
        root.height = 1 + max(self.height(root.left), self.height(root.right)) 
        b = self.balance(root) 
        if b > 1 and data < root.left.data: 
            return self.right_rotate(root) 
        if b < -1 and data > root.right.data: 
            return self.left_rotate(root) 
        if b > 1 and data > root.left.data: 
            root.left = self.left_rotate(root.left) 
            return self.right_rotate(root) 
        if b < -1 and data < root.right.data: 
            root.right = self.right_rotate(root.right) 
            return self.left_rotate(root) 
        return root 
    def search(self, root, data): 
        if root is None: 
            return False 
        if root.data == data: 
            return True 
        elif data < root.data: 
            return self.search(root.left, data) 
        else: 
            return self.search(root.right, data) 
    def find_min(self, root): 
        current = root 
        while current.left is not None: 
            current = current.left 
        return current 
    def delete(self, root, data): 
        if root is None: 
            return root 
        if data < root.data: 
            root.left = self.delete(root.left, data) 
        elif data > root.data: 
            root.right = self.delete(root.right, data) 
        else: 
            if root.left is None: 
                return root.right 
            elif root.right is None: 
                return root.left 
            else: 
                temp = self.find_min(root.right) 
                root.data = temp.data 
                root.right = self.delete(root.right, temp.data) 
        root.height = 1 + max(self.height(root.left), self.height(root.right)) 
        b = self.balance(root) 
        if b > 1 and self.balance(root.left) >= 0: 
            return self.right_rotate(root) 
        if b > 1 and self.balance(root.left) < 0: 
            root.left = self.left_rotate(root.left) 
            return self.right_rotate(root) 
        if b < -1 and self.balance(root.right) <= 0: 
            return self.left_rotate(root) 
        if b < -1 and self.balance(root.right) > 0: 
            root.right = self.right_rotate(root.right) 
            return self.left_rotate(root) 
        return root 
    def inorder(self, root): 
        if root: 
            self.inorder(root.left) 
            print(root.data, end=" ") 
            self.inorder(root.right) 
    def preorder(self, root): 
        if root: 
            print(root.data, end=" ") 
            self.preorder(root.left) 
            self.preorder(root.right) 
    def postorder(self, root): 
        if root: 
            self.postorder(root.left) 
            self.postorder(root.right) 
            print(root.data, end=" ") 
    def level_order(self, root): 
        if root is None: 
            return 
        queue = [root] 
        while queue: 
            node = queue.pop(0) 
            print(node.data, end=" ") 
            if node.left: 
                queue.append(node.left) 
            if node.right: 
                queue.append(node.right) 
 
print("G.MOKSHAGNASAI...AV.SC.U4CSE25111...") 
avl = AVLTree() 
root = None 
 
while True: 
    print("\n\n--- AVL TREE ---") 
    print("1. Insert") 
    print("2. Search") 
    print("3. Delete") 
    print("4. Inorder Traversal") 
    print("5. Preorder Traversal") 
    print("6. Postorder Traversal") 
    print("7. Level Order Traversal") 
    print("8. Exit")  
    choice = int(input("Enter your choice: ")) 
 
    if choice == 1: 
        data = int(input("Enter value to insert: ")) 
        root = avl.insert(root, data) 
        print("Node inserted successfully.") 
    elif choice == 2: 
        data = int(input("Enter value to search: ")) 
        if avl.search(root, data): 
            print("Element found.") 
        else: 
            print("Element not found.") 
    elif choice == 3: 
        data = int(input("Enter value to delete: ")) 
        root = avl.delete(root, data) 
        print("Node deleted successfully.") 
    elif choice == 4: 
        print("Inorder Traversal:") 
        avl.inorder(root) 
    elif choice == 5: 
        print("Preorder Traversal:") 
        avl.preorder(root) 
    elif choice == 6: 
        print("Postorder Traversal:") 
        avl.postorder(root) 
    elif choice == 7: 
        print("Level Order Traversal:") 
        avl.level_order(root) 
    elif choice == 8: 
        print("Program terminated.") 
        break 
    else: 
        print("Invalid choice.")
