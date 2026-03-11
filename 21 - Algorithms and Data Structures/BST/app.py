from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(10))
tree.add(Node(15))
tree.add(Node(5))
tree.add(Node(3))
tree.add(Node(7))
tree.add(Node(12))
tree.add(Node(17))

print("Binary Search Tree Structure:")
print("=" * 30)
tree.print_tree()
