class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        h = [[float('inf')] * n for i in range(m)]
        h[0][0] = 0
        q = []
        heapq.heappush(q, (0, 0, 0))
        dir = [0, 1, 0, -1, 0]
        vis = []

        while q:
            w, i, j = heapq.heappop(q)
            if w > h[i][j]:
                continue 
            for d in range(4):
                x = i + dir[d]
                y = j + dir[d+1]
                if x>=0 and x<m and y>=0 and y<n:
                    dist = max(abs(heights[i][j] - heights[x][y]), h[i][j])
                    if dist < h[x][y]:
                        h[x][y] = dist
                        heapq.heappush(q, (dist, x, y))
                        # print(f" {i} {j} {x} {y} {dist}")

        return h[m-1][n-1]

                    

            
            

        