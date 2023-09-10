from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 1
        tmp = head
        cur = head
        while cur.next:
            cur = cur.next
            length += 1  
        cur.next = head

        k %= length
        cur = head
        for _ in range(length-k-1):
            cur = cur.next
        
        tmp = cur.next
        cur.next = None

        return tmp        