class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        def rec(idx, temp):
            ans.add(tuple(temp[:]))
            print(ans)
            for i in range(idx, n):
                temp.append(nums[i])
                rec(i+1, temp)
                temp.pop()

        rec(0, [])
        return ans
        