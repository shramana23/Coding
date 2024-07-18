class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum = 0
        ans = 0
        mp = {}
        mp[0] = 1

        for n in nums:
            sum += n
            diff = sum - k
            if diff in mp:
                ans += mp[diff]
            if sum not in mp:
                mp[sum] = 1
            else:
                mp[sum] += 1

        return ans
        