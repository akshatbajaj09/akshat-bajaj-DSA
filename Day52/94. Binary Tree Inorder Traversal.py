# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        ans = []
        st = []
        curr = root
        while curr or st:
            # Go to extreme left:
            while curr:
                st.append(curr)
                curr = curr.left
            # Now we go to the root in our order of left -> root -> right:
            curr = st.pop()
            ans.append(curr.val)
            # Move to the right subtree:
            curr = curr.right
        return ans
