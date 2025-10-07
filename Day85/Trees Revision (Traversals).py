# Preorder:
# Method - 1 (Recursive):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root):
        if not root:
            return self.ans
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        return self.ans

    def preorderTraversal(self, root):
        self.ans = []
        self.preorder(root)
        return self.ans


# Method - 2 (Iterative):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        curr, st, ans = root, [], []
        while curr or st:
            if curr:
                ans.append(curr.val)
                st.append(curr.right)
                curr = curr.left
            else:
                curr = st.pop()
        return ans


# Post-order:


# Method - 1 (Recursive):


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root):
        if not root:
            return self.ans
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)
        return self.ans

    def postorderTraversal(self, root):
        self.ans = []
        self.postorder(root)
        return self.ans


# Method - 2 (Iterative by modifying preorder and using reversal):


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        curr, st, ans = root, [], []
        while curr or st:
            if curr:
                ans.append(curr.val)
                st.append(curr.left)
                curr = curr.right
            else:
                curr = st.pop()
        return ans[::-1]


# Method - 3 (Iterative using single stack):
# This approach keeps a track of visited nodes and then iterates and appends in the
# final ans list acoordingly, and will be worked on later.
