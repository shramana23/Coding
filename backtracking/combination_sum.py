class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        candidates.sort()
        def rec(idx, temp, sum):
            if sum == target:
                ans.append(temp[:])
            if sum > target:
                return
            if candidates[idx] > target - sum:
                return
            for i in range(idx, n):
                temp.append(candidates[i])
                rec(i, temp, sum + candidates[i])
                temp.pop()

        rec(0, [], 0)
        return ans
        