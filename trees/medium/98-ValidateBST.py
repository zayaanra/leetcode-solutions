from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def inorder(left, right, cur):
            if not cur:
                return True
            if left < cur.val < right:
                return inorder(left=left, right=cur.val, cur=cur.left) and inorder(left=cur.val, right=right, cur=cur.right)
            else:
                return False
            

        return inorder(float("-inf"), float("inf"), root) and inorder(float("-inf"), float("inf"), root)