# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        # Base case:
        if not root:
            return
        # Recursive case:
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)

    def inorderTraversal(self, root):
        self.ans = []
        self.inorder(root)
        return self.ans
