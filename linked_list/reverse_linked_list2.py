# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        h = ListNode()
        h.next = head
        start = head
        prev = h

        for i in range(left-1):
            start = start.next 
            prev = prev.next

        end = start
        for i in range(right - left + 1):
            end = end.next
        
        for i in range(right - left + 1):
            nxt = start.next
            start.next = end
            end = start
            start = nxt

        prev.next = end

        return h.next
        

        

        
