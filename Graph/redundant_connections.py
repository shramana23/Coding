class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ln = len(edges)
        parents = list(range(ln+1))
        ranks = [1] * (ln+1)

        def find_parents(src):
            if parents[src] == src:
                return src
            parents[src] = find_parents(parents[src])
            return parents[src]

        def union(u, v):
            pu = find_parents(u)
            pv = find_parents(v)
            if pu == pv:
                return False

            if ranks[pu] > ranks[pv]:   
                parents[pv] = pu
            elif ranks[pv] > ranks[pu]:
                parents[pu] = pv
            else:
                parents[pu] = pv
                ranks[pv] += 1
            # print(parents)
            return True


        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
    
        