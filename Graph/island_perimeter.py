class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def is_valid(i, j):
            return i>=0 or i<m or j>=0 or j<n

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 4
                    if is_valid(i-1, j) and grid[i-1][j] == -1:
                        ans -= 2
                    if is_valid(i, j-1) and grid[i][j-1] == -1:
                        ans -= 2
                    grid[i][j] = -1

        return ans

        