class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        n = len(nums)
        start = 0
        end = 0
        i = 0
        ans = 0
        count = 0
        temp = 0

        while(i < n):
            if nums[i] == target:
                count += 1

            while count >= k:
                if nums[start] == target:
                    count -= 1
                start += 1

            print(i, start)

            ans += start
            i += 1

        return ans

                
                
        