class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_oranges += 1
        dir = [0, 1, 0, -1, 0]
        ans = 0
        # print(q)
        while q:
            # print(q)
            ln = len(q)
            if fresh_oranges == 0:
                return ans
            for l in range(ln):
                i, j = q.popleft()
                for d in range(4):
                    x = i + dir[d]
                    y = j + dir[d+1]

                    if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                        grid[x][y] = 2
                        # print(x)
                        # print(y)
                        q.append((x, y))
                        fresh_oranges -= 1
            ans += 1
        
        if fresh_oranges != 0:
            return -1
        
        return 0



        