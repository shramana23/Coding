class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp = [float('inf')] * n

        # dp[0] = 1
        max_reach = 0

        for i in range(n):
            if nums[i] == 0:
                continue
            if i>max_reach:
                return False
            max_idx = min(i+nums[i], n-1)
            # print(i)
            # print(max_idx)
            # dp[max_idx] = 1
            max_reach = max(max_reach, max_idx)

        # print(dp)

        return True

         

        