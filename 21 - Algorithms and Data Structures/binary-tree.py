# binary tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def search(self, value):
        if value == self.value:
            return True
        if value < self.value:
            if self.left is None:
                return False
            return self.left.search(value)
        if value > self.value:
            if self.right is None:
                return False
            return self.right.search(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_value = self.right.find_min()
            self.value = min_value
            self.right = self.right.delete(min_value)
        return self

    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.value
        return self.right.find_max()

    def count_nodes(self):
        left_count = self.left.count_nodes() if self.left else 0
        right_count = self.right.count_nodes() if self.right else 0
        return 1 + left_count + right_count

    def count_leaves(self):
        if self.left is None and self.right is None:
            return 1
        left_leaves = self.left.count_leaves() if self.left else 0
        right_leaves = self.right.count_leaves() if self.right else 0
        return left_leaves + right_leaves

    def count_internal_nodes(self):
        if self.left is None and self.right is None:
            return 0
        left_internal = self.left.count_internal_nodes() if self.left else 0
        right_internal = self.right.count_internal_nodes() if self.right else 0
        return 1 + left_internal + right_internal

    def height(self):
        if self.left is None and self.right is None:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def is_balanced(self):
        if self.left is None and self.right is None:
            return True
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return abs(left_height - right_height) <= 1

    def is_complete(self):
        if self.left is None and self.right is None:
            return True
        if self.left is None or self.right is None:
            return False
        return self.left.is_complete() and self.right.is_complete()

    def is_full(self):
        if self.left is None and self.right is None:
            return True
        if self.left is None or self.right is None:
            return False
        return self.left.is_full() and self.right.is_full()

    def is_perfect(self):
        if self.left is None and self.right is None:
            return True
        if self.left is None or self.right is None:
            return False
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return left_height == right_height

    def is_bst(self):
        if self.left is None and self.right is None:
            return True
        if self.left is None or self.right is None:
            return False
        if self.left.value > self.value:
            return False
        if self.right.value < self.value:
            return False
        return self.left.is_bst() and self.right.is_bst()

    def is_bst2(self):
        if self.left is None and self.right is None:
            return True
        if self.left is None or self.right is None:
            return False
        if self.left.value > self.value:
            return False
        if self.right.value < self.value:
            return False
        return self.left.is_bst2() and self.right.is_bst2()

    def is_bst3(self):
        if self.left is None and self.right is None:
            return True
        if self.left is None or self.right is None:
            return False
        if self.left.value > self.value:
            return False
        if self.right.value < self.value:
            return False
        return self.left.is_bst3() and self.right.is_bst3()

    def is_bst4(self):
        if self.left is None and self.right is None:
            return True
        if self.left is None or self.right is None:
            return False
        if self.left.value > self.value:
            return False
        if self.right.value < self.value:
            return False
        return self.left.is_bst4() and self.right.is_bst4()


n = Node(5)
n.insert(3)
n.insert(7)
n.insert(2)
n.insert(4)
n.insert(6)
n.insert(8)
n.print_tree()

print("Min:", n.find_min())
print("Max:", n.find_max())
print("Count nodes:", n.count_nodes())
print("Count leaves:", n.count_leaves())
print("Count internal nodes:", n.count_internal_nodes())
print("Height:", n.height())
print("Is balanced:", n.is_balanced())
print("Is complete:", n.is_complete())
print("Is full:", n.is_full())
print("Is perfect:", n.is_perfect())
print("Is BST:", n.is_bst())
print("Is BST2:", n.is_bst2())
print("Is BST3:", n.is_bst3())
print("Is BST4:", n.is_bst4())


# Output:
# 5
# 3 7
# 2 4 6 8
# Min: 2
# Max: 8
# Count nodes: 7
# Count leaves: 4
# Count internal nodes: 3
# Height: 3
# Is balanced: True
# Is complete: True
# Is full: False
# Is perfect: False
# Is BST: True
# Is BST2: True
# Is BST3: True
# Is BST4: True
