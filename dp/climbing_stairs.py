class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        second = 1
        first = 1
        curr = 0
        for i in range(2, n+1):
            curr = second + first
            second = first 
            first = curr

        return curr 





        