class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        probs = [0] * n
        probs[start_node] = 1
        i = 0
        for s, d in edges:
            adj[s].append((d, succProb[i]))
            adj[d].append((s, succProb[i]))
            i += 1

        q = []
        heapq.heappush(q, (-1, start_node))
        while q:
            w, node = heapq.heappop(q)
            w *= -1
            if node == end_node:
                return w
            if w < probs[node]:
                continue
            
            for d, p in adj[node]:
                prob = w * p 

                if prob > probs[d]:
                    probs[d] = prob
                    heapq.heappush(q, (-prob, d))            
        
        return 0