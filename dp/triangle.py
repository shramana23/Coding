class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = []

        for i in range(m-1):
            dp = [float('inf')] * (len(triangle[i]) + 1)
            for j in range(i+1):
                dp[j] = min(dp[j], triangle[i][j] + triangle[i+1][j])
                dp[j+1] = min(dp[j+1], triangle[i][j] + triangle[i+1][j+1])

            triangle[i+1][:] = dp[:]
        # print(triangle)
            
        return min(triangle[-1])


