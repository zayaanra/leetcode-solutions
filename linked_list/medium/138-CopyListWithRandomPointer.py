from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}

        old = head
        while old:
            new = Node(old.val)
            oldToNew[old] = new
            old = old.next
        
        old = head
        while old:
            new = oldToNew[old]
            new.next = oldToNew[old.next]
            new.random = oldToNew[old.random]
            old = old.next
        return oldToNew[head]