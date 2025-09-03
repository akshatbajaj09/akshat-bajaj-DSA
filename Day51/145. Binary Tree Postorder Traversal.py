# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root):
        # Base case:
        if not root:
            return
        # Recursive case:
        self.postorder(root.left)  # Left subtree
        self.postorder(root.right)  # Right subtree
        self.ans.append(root.val)

    def postorderTraversal(self, root):
        self.ans = []
        self.postorder(root)
        return self.ans
