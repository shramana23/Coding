class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        # if odd
        if totalSum % 2 == 1:
            return False

        ourTarget = totalSum // 2

        n = len(nums)
        dp = [[-1] * (ourTarget+1) for _ in range(n+1)]

        def rec(idx, target):
            if idx == 0:
                return nums[idx] == target
            
            if target == 0:
                return True

            if dp[idx][target] != -1:
                return dp[idx][target]

            not_take = rec(idx - 1, target)
            take = rec(idx - 1, target - nums[idx])

            dp[idx][target] = take or not_take

            return dp[idx][target]
        return rec(n-1, ourTarget)


        



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        # if odd
        if totalSum % 2 == 1:
            return False

        ourTarget = totalSum // 2

        n = len(nums)
        dp = [[0] * (ourTarget+1) for _ in range(n+1)]
        dp[0][0] = 1

        # def rec(idx, target):
        #     if idx == 0:
        #         return nums[idx] == target
            
        #     if target == 0:
        #         return True

        #     if dp[idx][target] != -1:
        #         return dp[idx][target]

        #     not_take = rec(idx - 1, target)
        #     take = rec(idx - 1, target - nums[idx])

        #     dp[idx][target] = take or not_take

        #     return dp[idx][target]

        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, ourTarget+1):
                not_take = dp[i - 1][j]
                take = False
                if j>= nums[i-1]:
                    take = dp[i - 1][j - nums[i-1]]

                dp[i][j] = take or not_take
        
        return dp[n][ourTarget]


        