# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root):
        # Base case:
        if not root:
            return
        # Recursive case:
        self.ans.append(root.val)
        self.preorder(root.left)  # Left subtree
        self.preorder(root.right)  # Right subtree

    def preorderTraversal(self, root):
        self.ans = []
        self.preorder(root)
        return self.ans
