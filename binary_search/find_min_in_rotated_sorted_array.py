class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1  

        while(l<=r):
            if nums[r] >= nums[l]:
                return nums[l]
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                l = mid + 1 
            else:
                r = mid
        