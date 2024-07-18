# leetcode - https://leetcode.com/problems/maximum-subarray/description/

nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = 0 

class solution:
    """
        Storing at dp[i] the max subarray sum possible inclding ith value
    """
    def func(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i, n in enumerate(nums):
            if i == 0:
                continue
            dp[i] = max(dp[i-1] + n, n)
        return max(dp)

s = solution()
s.func(nums)


def better_solution(nums):
    if not nums:
        return 0

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
