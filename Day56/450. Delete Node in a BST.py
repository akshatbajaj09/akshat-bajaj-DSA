# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        # Search the node to be deleted:
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # We don't need an explicit case for:
            # if (not root.left) and (not root.right):
            #     return None
            # As if the root.left is None then the first if block hits true
            # and returns root.right which may also be None and hence will
            # return None, however if root.right is not None
            # then it gets returned anyway.
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Find min node in right subtree:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
        return root
