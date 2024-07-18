class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = list(range(n))
        # ranks = [1] * n

        ans = n

        def find(src):
            if parents[src] == src:
                return src

            parents[src] = find(parents[src])
            return parents[src]

        def union(u, v):
            # print(u)
            # print(v)
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return 0

            parents[pu] = pv
           
            return 1

        for u in range(n):
            for v in range(n):
                if u != v and isConnected[u][v] == 1:
                    ans -= union(u, v)

        return ans

        