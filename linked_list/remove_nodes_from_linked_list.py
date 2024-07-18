# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rec(curr):
            if not curr.next:
                return curr
            
            curr.next = rec(curr.next)

            if curr.next and curr.val < curr.next.val:
                return curr.next

            return curr

        temp = head
        return rec(temp)

            
                
        