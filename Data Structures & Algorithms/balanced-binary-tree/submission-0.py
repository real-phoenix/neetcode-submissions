# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        def dfs(cur):
            if not cur:
                return 0 

            left = dfs(cur.left)
            right = dfs(cur.right)
            val = abs(left-right)
            if val>1:
                self.flag = False
            return 1 + max(left, right)
        dfs(root)
        return self.flag