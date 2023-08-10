# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(root, greatest):
            nonlocal good
            if not root:
                return
            
            if root.val >= greatest:
                good += 1
            
            greatest = max(greatest, root.val)
            dfs(root.left, greatest)
            dfs(root.right, greatest)
        
        dfs(root, root.val)
        return good