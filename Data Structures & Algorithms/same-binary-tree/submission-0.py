# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag = True
        def dfs(p, q):
            if not p:
                if q:
                    self.flag = False
                return None
            if not q:
                if p:
                    self.flag = False
                return None
            # print(p.val, q.val)
            if p and q and p.val != q.val:
                self.flag = False
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return
        dfs(p,q)
        return self.flag
