from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length = 0
        def dfs(root):
            nonlocal length
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            length = max(length, l + r)
            return 1 + max(l, r)
        
        dfs(root)
        return length