class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = {}

        for i in range(n):
            if nums[i] not in mp:
                mp[nums[i]] = i
            else:
                j = mp[nums[i]]
                if abs(i - j) <=k:
                    return True
                mp[nums[i]] = i

        return False

        