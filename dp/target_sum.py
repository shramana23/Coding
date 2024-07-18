class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        targetSum = sum(nums)
        if (targetSum - target) < 0 or target < - targetSum or (targetSum - target) % 2 != 0:
            return 0
        s2 = (targetSum - target) // 2

        n = len(nums)
        dp = [[0] * (s2+1) for _ in range (n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, s2+1):
                dp[i][j] += dp[i-1][j] 
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j - nums[i-1]]
        return dp[-1][-1]
        
            