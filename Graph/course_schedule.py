class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)
        
        vis = [0] * numCourses
        dfsVis = [0] * numCourses

        def is_cycle(src):
            vis[src] = True
            dfsVis[src] = True

            for n in adj[src]:
                if dfsVis[n]:
                    return True
                if not vis[n]:
                    if is_cycle(n):
                        return True
            dfsVis[src] = False

            return False

        for i in range(numCourses):
            if is_cycle(i):
                return False

        return True

        

        

        