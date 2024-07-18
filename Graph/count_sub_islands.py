class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])
        dir = [0, 1, 0, -1, 0]

        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j] == 0:
                return 1
            res = 1
            if grid1[i][j] != grid2[i][j]:
                res = 0
            grid2[i][j] = 0

            for d in range(4):
                if not dfs(i+dir[d], j+dir[d+1]):
                    res = 0
            
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    ans += dfs(i, j)

        return ans





        