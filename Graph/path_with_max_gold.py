class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0

        def dfs(i, j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0:
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            res = val + max(dfs(i+1, j), dfs(i, j+1), dfs(i-1, j), dfs(i, j-1))
            # ans = max(ans, res)
            grid[i][j] = val
            return res


        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))

        return ans



        