class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            diff = hash.get(target - n, -1)
            if diff != -1:
                return [i, diff]
            hash[n] = i
        return [-1, -1]

        


        