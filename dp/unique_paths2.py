class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
        print(dp)
        return dp[m-1][n-1]