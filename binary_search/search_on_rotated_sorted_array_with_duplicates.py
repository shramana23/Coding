class Solution:
    def search_range(self, nums, target, l, r):
        if l > r:
            return False
        mid = (l + r) // 2
        if nums[mid] == target:
            return True

        if nums[mid] == nums[l]:
            return self.search_range(nums, target, l+1, r)
        if nums[mid] == nums[r]:
            return self.search_range(nums, target, l, r-1)
        if nums[l] <= nums[mid]:
            if nums[l] <= target <= nums[mid]:
                return self.search_range(nums, target, l, mid - 1)
            else:
                return self.search_range(nums, target, mid + 1, r)
        else:
            if nums[mid] <= target <= nums[r]:
                return self.search_range(nums, target, mid + 1, r)
            else:
                return self.search_range(nums, target, l, mid - 1)
        return False
    def search(self, nums: List[int], target: int) -> bool:
        return self.search_range(nums, target, 0, len(nums)-1)
