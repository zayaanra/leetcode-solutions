from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            l, r = max(l, 0), max(r, 0)
            total = root.val + l + r
            res = max(res, total)
            return root.val + max(l, r)

        dfs(root)
        return res
        