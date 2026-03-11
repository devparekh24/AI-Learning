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
        """Print the tree with nodes connected by / and \\ edges."""
        if not self.head:
            print("Tree is empty")
            return

        height = self._get_height(self.head)
        total_width = (1 << height) * 2  # generous canvas width

        # BFS: track (node, lo, hi) bounds; each node's column = (lo+hi)//2
        levels = []
        current = [(self.head, 0, total_width - 1)]

        for _ in range(height):
            levels.append(current)
            next_level = []
            for node, lo, hi in current:
                mid = (lo + hi) // 2
                if node:
                    next_level.append((node.left, lo, mid - 1))
                    next_level.append((node.right, mid + 1, hi))
                else:
                    next_level.append((None, lo, mid - 1))
                    next_level.append((None, mid + 1, hi))
            current = next_level

        for level_idx, level in enumerate(levels):
            # Node row
            row = [' '] * total_width
            for node, lo, hi in level:
                if node:
                    mid = (lo + hi) // 2
                    val = str(node.value)
                    start = mid - len(val) // 2
                    for i, ch in enumerate(val):
                        if 0 <= start + i < total_width:
                            row[start + i] = ch
            print(''.join(row).rstrip())

            # Edge row (skip for last level)
            if level_idx >= height - 1:
                continue

            edge_row = [' '] * total_width
            next_lvl = levels[level_idx + 1]
            for i, (node, lo, hi) in enumerate(level):
                if not node:
                    continue
                parent_mid = (lo + hi) // 2
                left_child, left_lo, left_hi = next_lvl[i * 2]
                right_child, right_lo, right_hi = next_lvl[i * 2 + 1]
                if left_child:
                    child_mid = (left_lo + left_hi) // 2
                    for c in range(child_mid + 1, parent_mid):
                        edge_row[c] = '/'
                if right_child:
                    child_mid = (right_lo + right_hi) // 2
                    for c in range(parent_mid + 1, child_mid):
                        edge_row[c] = '\\'
            print(''.join(edge_row).rstrip())

    def _get_height(self, node):
        """Get the height of the tree."""
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))
