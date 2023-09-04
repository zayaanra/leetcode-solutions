from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getKthNode(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupTail = ListNode(0, head)

        while True:
            kNode = self.getKthNode(groupTail, k)
            # no more nodes left
            if not kNode:
                break
            groupTail.next = kNode
            groupHead = kNode.next

            prev, cur = groupHead, head
            while cur != groupHead:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            groupTail = head
            head = groupHead


        return dummy.next