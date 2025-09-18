# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invert(root.left)
        self.invert(root.right)
        return root

    def invertTree(self, root):
        self.invert(root)
        return root

    # Method - 2 (Iterative approach):

    def invertTree2(self, root):
        if not root:
            return None
        st = []
        curr = root
        while curr or st:
            while curr:
                st.append(curr)
                curr.left, curr.right = curr.right, curr.left
                curr = curr.left
            curr = st.pop()
            curr = curr.right
        return root
