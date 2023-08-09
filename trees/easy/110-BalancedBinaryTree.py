from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ok = True
        def dfs(root):
            nonlocal ok
            if not root:
                return 0
            
            l, r = dfs(root.left), dfs(root.right)
            if abs(l - r) > 1:
                ok = False
            return 1 + max(l, r)
        
        dfs(root)
        return ok