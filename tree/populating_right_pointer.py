"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            ln = len(q)
            nodel = None
            for i in range(ln):
                noder = q.popleft()
                if i > 0:  
                    nodel.next = noder
                nodel = noder
                if nodel.left:
                    q.append(nodel.left)
                if nodel.right:
                    q.append(nodel.right)
        return root
            



        