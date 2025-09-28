# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# I tried doing return p == q directly but p and q being seperate objects having different
# memory locations will always output False for p == q.
# But if we modify the __eq__ method in the class itself to return p == q the way we want
# then this could be solved more cleverly but leetcode doesn't allow us to modify or
# customize methods like __eq__ and hence the algorithmic thinking is the only work around.
