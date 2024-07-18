class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zs = nums.count(0)
        os = nums.count(1)
        ts = nums.count(2)
        
        zarr = [0] * zs
        oarr = [1] * os
        tarr = [2] * ts

        nums[:] = zarr + oarr + tarr




        