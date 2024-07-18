# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        ptr1 = l1
        ptr2 = l2

        ans = ListNode()
        temp = ans

        while(ptr1 or ptr2):
            v1 = ptr1.val if ptr1 else 0
            v2 = ptr2.val if ptr2 else 0
            total = v1 + v2 + c 
            temp.next = ListNode(total % 10)
            temp = temp.next 
            c = total // 10
            if ptr1:
                ptr1 = ptr1.next 
            if ptr2:
                ptr2 = ptr2. next
        if c:
            temp.next = ListNode(c)
        return ans.next

        