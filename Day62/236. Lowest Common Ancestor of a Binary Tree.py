# Yesterday's code of Lowest Common Ancestor of a Binary Tree:


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def inorderTraversal(self, root):
#         ans = []
#         st = []
#         curr = root
#         while curr or st:
#             while curr:
#                 st.append(curr)
#                 curr = curr.left
#             curr = st.pop()
#             ans.append(curr.val)
#             curr = curr.right
#         return ans

#     def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
#         inorder = self.inorderTraversal(root)
#         curr = root
#         for i in range(len(inorder)):
#             if inorder[i] == p.val:
#                 ind_p = i
#                 print(ind_p)
#             if inorder[i] == q.val:
#                 ind_q = i
#                 print(ind_q)
#             if inorder[i] == curr.val:
#                 ind_curr = i
#                 print(ind_curr)
#         while True:
#             if ind_p < ind_curr and ind_q < ind_curr:
#                 curr = curr.left
#             elif ind_p > ind_curr and ind_q > ind_curr:
#                 curr = curr.right
#             else:
#                 return curr
#             if not curr:
#                 return None


# The error in above code:

# ind_curr was not being updated everytime we did curr = curr.left or curr = curr.right

# Fix:

# A simple fix is to find the index for every iteration within the while loop.

# Readability:

# We can also skip the last if block of:
# if not curr:
#     return None
# and simply use while curr instead of while True and then return None as a fallback.

# Final code:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        ans = []
        st = []
        curr = root
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        inorder = self.inorderTraversal(root)
        curr = root
        while curr:
            for i in range(len(inorder)):
                if inorder[i] == p.val:
                    ind_p = i
                if inorder[i] == q.val:
                    ind_q = i
                if inorder[i] == curr.val:
                    ind_curr = i
            if ind_p < ind_curr and ind_q < ind_curr:
                curr = curr.left
            elif ind_p > ind_curr and ind_q > ind_curr:
                curr = curr.right
            else:
                return curr
        return None


# Method - 2 (Recursive approach):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor2(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right
