class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def rec(idx, temp):
            ans.append(temp[:])
            print(ans)
            for i in range(idx, n):
                temp.append(nums[i])
                rec(i+1, temp)
                temp.pop()

        rec(0, [])
        return ans
            

        