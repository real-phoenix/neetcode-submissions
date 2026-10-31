# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        root_max = root.val
        def good_nodes(node, mxx_val):
            nonlocal ans 
            if not node:
                return
            if node.val >= mxx_val:
                ans+=1
            mxx_val = max(mxx_val, node.val)
            good_nodes(node.left, mxx_val)
            good_nodes(node.right, mxx_val)
            return
        good_nodes(root, root_max)
        return ans
