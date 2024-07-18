# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head 
        n = 1
        while temp.next:
            temp = temp.next
            n += 1
        
        k = k % n 

        if k == 0:
            return head

        curr = head 

        for i in range(n-k-1):
            curr = curr.next 

        start = curr.next 

        temp.next = head
        curr.next = None

        return start

        