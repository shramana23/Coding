class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for u, v, w in times:
            adjList[u].append((w, v))
        
        heap = []
        heapq.heappush(heap, (0, k))

        vis = set()

        while heap:
            dist, node = heapq.heappop(heap)
            vis.add(node)

            if len(vis) == n:
                return dist

            for w, a in adjList[node]:
                if a not in vis:
                    heapq.heappush(heap, (w+dist, a))
        return -1

        