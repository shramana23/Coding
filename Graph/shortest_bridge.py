class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = set()
        dir = [0, 1, 0, -1, 0]

        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0:
                return
            grid[i][j] = 0
            vis.add((i, j))
            for d in range(4):
                dfs(i+dir[d], j+dir[d+1])

        def bfs():
            q = deque(vis)
            res = 0
            while q:
                ln = len(q)
                for l in range(ln):
                    i, j = q.popleft()
                    for d in range(4):
                        x = i + dir[d]
                        y = j + dir[d+1]
                        if 0<=x<m and 0<=y<n and (x, y) not in vis:
                            if grid[x][y] == 1:
                                return res
                            q.append((x, y))
                            vis.add((x, y))
                res += 1


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    # print(vis)
                    return bfs()



        