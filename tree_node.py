class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root= TreeNode('1')
node2=TreeNode('2')
node3=TreeNode('3')
node4=TreeNode('4')
node5=TreeNode('5')
node6=TreeNode('6')
node7=TreeNode('7')
node8=TreeNode('8')
node9=TreeNode('9')
node10=TreeNode('10')

root.left=node2
root.right=node3

node2.left=node4
node2.right=node5

node5.left=node8

node3.left=node6
node3.right=node7

node7.left=node9
node7.right=node10
# Preorder: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Inorder: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
        
# Postorder: Left -> Right -> Root
def levelorder(root):
    if root:
        levelorder(root.left)
        levelorder(root.right)
        print(root.data, end=" ")



# Print all traversals
print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

print("\nLevel Order:")
levelorder(root)
