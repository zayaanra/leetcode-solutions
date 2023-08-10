from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []


        res = []
        q = deque()
        q.append(root)
        while q:
            curLevel = []
            for i in range(len(q)):
                v = q.popleft()
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
                curLevel.append(v.val)
            res.append(curLevel)
            
        return res