class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to construct a binary tree from user input
def constructTree(nodes):
    if nodes <= 0:
        return None

    data = input("Enter node value: ")
    node = Node(int(data))

    left_nodes = int(input("Enter number of nodes in the left subtree: "))
    node.left = constructTree(left_nodes)

    right_nodes = int(input("Enter number of nodes in the right subtree: "))
    node.right = constructTree(right_nodes)

    return node

# Traversing the tree (pre-order traversal)
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

# Get the number of nodes in the binary tree from the user
num_nodes = int(input("Enter the number of nodes in the binary tree: "))

# Create the binary tree based on user input
print("Enter the values to construct the binary tree:")
root = constructTree(num_nodes)

# Perform pre-order traversal
print("Pre-order traversal: ", end="")
preorder(root)
