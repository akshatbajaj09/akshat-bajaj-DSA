# Inorder Traversal:
# Method - 1:
# Recursive:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if not root:
            return self.ans
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)
        return self.ans

    def inorderTraversal(self, root):
        self.ans = []
        self.inorder(root)
        return self.ans


# Method - 2:
# Iterative:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        curr, st, ans = root, [], []
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans
