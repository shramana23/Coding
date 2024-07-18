class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 0
        l = 0
        r = 1
        n = len(nums)
        count = 1

        while(r<n):
            if nums[r] != nums[last]:
                l += 1
                nums[l] = nums[r]
                last = l
                count = 1
            else:
                count += 1
                if count < 3:
                    l += 1
                    nums[l] = nums[r]
            r += 1


        return l+1
