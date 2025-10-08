# Method - 3 (In continuation of Day 85):
# Iterative method using single stack and no reversal:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        curr, st, ans, last_visited = root, [], [], None
        while curr or st:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                peek = st[-1]
                if not peek.right or peek.right == last_visited:
                    peek = st.pop()
                    ans.append(peek.val)
                    last_visited = peek
                else:
                    curr = peek.right
        return ans
