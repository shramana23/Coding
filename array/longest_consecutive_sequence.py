class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = {}
        ans = 0

        for n in nums:
            if n in hash:
                continue
            l = hash.get(n-1, 0)
            r = hash.get(n+1, 0)
            hash[n] = l + r + 1
            hash[n-l] = hash[n]
            hash[n+r] = hash[n]

            ans = max(ans, hash[n])
        return ans


        