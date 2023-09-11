from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        ans = []
        q = deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                v = q.popleft()
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
                level.append(v.val)
            if len(ans) % 2 == 0:
                ans.append(level)
            else:
                ans.append(level[::-1])
                
        return ans