# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        new_head = ListNode()
        new_head.next = head
        ptr = new_head
        while ptr.next:
            if ptr.next.next and ptr.next.next.val == ptr.next.val:
                start = ptr.next.next.next
                while start and start.val == ptr.next.val:
                    start = start.next
                ptr.next = start
            else:
                ptr = ptr.next

        return new_head.next



        