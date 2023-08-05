from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        new = slow.next
        prev = slow.next = None
        # reverse second half of the linked list
        while new:
            tmp = new.next
            new.next = prev
            prev = new
            new = tmp
        
        # reorder the linked list
        cur = head
        while prev:
            t1, t2 = cur.next, prev.next
            cur.next = prev
            prev.next = t1
            cur, prev = t1, t2