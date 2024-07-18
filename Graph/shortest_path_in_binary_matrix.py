class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        m = len(grid)
        n = len(grid[0])
        vis = set()
        paths = [[float('inf')] * n for i in range(m)]
        paths[0][0] = 1

        q = []
        heapq.heappush(q, (1, 0, 0))
        vis.add((0,0))
        diri = [0, 1, -1]
        dirj = [0, 1, -1]

        while q:
            dist, i, j = heapq.heappop(q)
            if len(vis) == m * n:
                return dist
            
            for di in diri:
                for dj in dirj:
                    if di == 0 and dj == 0:
                        continue
                    x = i + di
                    y = j + dj
                    if 0<=x<m and 0<=y<n and grid[x][y] != 1:
                        nd = dist + 1
                        if (x, y) not in vis and nd < paths[x][y]:
                            paths[x][y] = nd
                            heapq.heappush(q, (nd, x, y))
                            vis.add((x, y))
                            # print(paths)
                        
        if paths[m-1][n-1] >= float('inf'):
            return -1
        
        return paths[m-1][n-1]
            




        
        