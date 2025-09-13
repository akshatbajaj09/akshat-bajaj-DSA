# The below solution is Incorrect and needs to be fixed (will do later)


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
        for i in range(len(inorder)):
            if inorder[i] == p.val:
                ind_p = i
                print(ind_p)
            if inorder[i] == q.val:
                ind_q = i
                print(ind_q)
            if inorder[i] == curr.val:
                ind_curr = i
                print(ind_curr)
        while True:
            if ind_p < ind_curr and ind_q < ind_curr:
                curr = curr.left
            elif ind_p > ind_curr and ind_q > ind_curr:
                curr = curr.right
            else:
                return curr
            if not curr:
                return None
