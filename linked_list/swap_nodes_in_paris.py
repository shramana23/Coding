# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode()
        h.next = head

        curr = h.next
        prev = h
        while curr and curr.next:
            nxt = curr.next.next
            second = curr.next 

            second.next = curr
            prev.next = second
            curr.next = nxt

            prev = curr
            curr = nxt

        return h.next
        

        