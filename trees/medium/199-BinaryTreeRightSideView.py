# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        view = []
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
            view.append(curLevel[-1])
        
        return view