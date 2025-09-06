# Method - 1 (Using functional programming):


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        # Base case:
        if not root:
            return 0
        # Recursive case:
        left = self.height(root.left)
        if left == -1:
            return -1
        right = self.height(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    def isBalanced(self, root):
        return self.height(root) != -1


# Method - 2 (Using OOP):


class Solution:
    def __init__(self):
        self.ans = True

    def height(self, root):
        # Base case:
        if not root:
            return 0
        # Recursive case:
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            self.ans = False
        return max(left, right) + 1

    def isBalanced(self, root):
        self.height(root)
        return self.ans


# Method - 1 is preferred over method - 2 because in method - 2 we get some side effects
# as the scope of one function is interacting with other which isn't preferred.
