class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        degrees = [0] * n
        # print(adj)
        q = deque()
        vis = [0] * n

        for i in range(n):
            a = adj[i]
            degrees[i] = len(a)
            if degrees[i] == 1:
                q.append(i)
                vis[i] = 1

        ans = []
        while q:
            # print(q)
            # print(degrees)
            ln = len(q)
            ans = list(q)
            for l in range(ln):
                node = q.popleft()
                for nd in adj[node]:
                    degrees[nd] -= 1
                    if degrees[nd] <= 1 and not vis[nd]:
                        q.append(nd)
                        vis[nd] = 1

        return ans
        