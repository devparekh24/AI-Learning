from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if current_node.value == new_node.value:
                raise ValueError(
                    f"Node with value {new_node.value} already exists in the tree."
                )
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def print_tree(self):
        """Print the entire tree in triangle form with nodes and edges."""
        if not self.head:
            print("Tree is empty")
            return

        # Get the height of the tree
        height = self._get_height(self.head)

        # Create the lines for each level
        lines = [[] for _ in range(height)]
        self._fill_lines(self.head, 0, lines)

        # Calculate spacing and print
        spacing = 4
        for level, line in enumerate(lines):
            level_spacing = spacing * (2 ** (height - level - 1))
            print(" " * (level_spacing // 2), end="")
            print((" " * level_spacing).join(str(node) for node in line))

    def _get_height(self, node):
        """Get the height of the tree."""
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _fill_lines(self, node, level, lines):
        """Fill the lines with node values level by level."""
        if node is None:
            return

        lines[level].append(node.value)
        self._fill_lines(node.left, level + 1, lines)
        self._fill_lines(node.right, level + 1, lines)
