# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')
        def rec(root):
            if not root:
                return 0

            ls = rec(root.left) 
            rs = rec(root.right)
            lh = ls + root.val
            rh = rs + root.val

            local_max = max(root.val, lh, rh, ls+rs+root.val)
            self.global_max = max(local_max, self.global_max)
            return max(root.val, lh, rh)

        rec(root)

        return self.global_max
        