class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # dp = [[0] * n for i in range(m)]

        # dp[0][0] = grid[0][0]
        for i in range(1,m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
            
        for j in range(1, n):
            grid[0][j] = grid[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        # print(dp)
        return grid[m-1][n-1]

        