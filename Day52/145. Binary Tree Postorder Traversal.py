# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Approach:
# To get "left -> right -> root" we will find "root -> right -> left" and reverse it.
# And to get "root -> right -> left" we will push left in stack first due to its property
# of LIFO (last in first out).


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        ans = []
        st = [root]
        while st:
            curr = st.pop()
            ans.append(curr.val)
            if curr.left:
                st.append(curr.left)
            if curr.right:
                st.append(curr.right)
        return ans[::-1]
