class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegrees = [0] * n
        outd = [0] * n 
        adj = defaultdict(list)

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                outd[i] += 1

        print(adj)
        print(outd)
        ans = []
        q = deque()
        for i in range(n):
            if outd[i] == 0:
                q.append(i)
                ans.append(i)

        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                for a in adj[node]:
                    outd[a] -= 1
                    if outd[a] == 0:
                        ans.append(a)
                        q.append(a)

        ans = sorted(ans)

        return ans



        