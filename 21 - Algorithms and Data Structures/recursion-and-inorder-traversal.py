# Implementation of Recursion and inorder traversal in Python


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )

    def preorderTraversal(self, root):
        if root is None:
            return []
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
        )

    def postorderTraversal(self, root):
        if root is None:
            return []
        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
        )

    def levelorderTraversal(self, root):
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def reverseLevelorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def reversePreorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def reversePostorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result

    def reverseInorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


tn = TreeNode()
tn.val = 1
tn.left = TreeNode(2)
tn.right = TreeNode(3)
tn.left.left = TreeNode(4)
tn.left.right = TreeNode(5)

s = Solution()
print(s.inorderTraversal(tn))
print(s.preorderTraversal(tn))
print(s.postorderTraversal(tn))
print(s.levelorderTraversal(tn))
print(s.reverseLevelorderTraversal(tn))
print(s.reversePreorderTraversal(tn))
print(s.reversePostorderTraversal(tn))
print(s.reverseInorderTraversal(tn))

# Output:
# [4, 2, 5, 1, 3]
# [1, 2, 4, 5, 3]
# [4, 5, 2, 3, 1]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]
# [4, 2, 5, 1, 3]

# Time Complexity: O(n)
# Space Complexity: O(n)
