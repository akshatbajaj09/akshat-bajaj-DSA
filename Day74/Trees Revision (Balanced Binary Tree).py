# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.difference = left - right if left > right else right - left
        if self.difference > 1:
            self.balanced = False
        return 1 + max(left, right)

    def isBalanced(self, root):
        self.balanced = True
        self.height(root)
        return self.balanced
