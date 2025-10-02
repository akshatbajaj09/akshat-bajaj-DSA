# Initial Approach:
# Traverse to a node which has no left or right child and then insert the val,
# according to the property of BST.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val):
        curr = root
        while curr.left or curr.right:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            print(curr)
        if val < curr.val:
            curr.left = TreeNode(val)
        else:
            curr.right = TreeNode(val)
        return root


# The above solution is wrong as:
# We missed the case when the root is None and we also missed the cases like:
# root = [4,7], val = 3 here the left child is None but the right child exists
# and we need to insert the val = 3 to TreeNode(4).left but the above logic applies
# curr = curr.left and makes curr as None, raising AttributeError:
# 'NoneType' object has no attribute 'left'

# Correct approach:


# Method - 1 (Iterative):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root, val):
        # Handling the edge case:
        if not root:
            return TreeNode(val)
        curr = root
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                else:
                    curr = curr.right


# Method - 2 (Recursive):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        curr = root
        if val < curr.val:
            curr.left = self.insertIntoBST(curr.left, val)
        else:
            curr.right = self.insertIntoBST(curr.right, val)
        return root
