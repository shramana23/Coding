from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def topological_sort_dfs(self):
        visited = set()
        stack = []
        
        # Helper function to perform DFS
        def dfs(v):
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(v)
        
        # Perform DFS for all vertices
        for vertex in list(self.graph):
            if vertex not in visited:
                dfs(vertex)
        
        # Return the topological order (reverse of stack)
        return stack[::-1]

# Example usage
g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort of the given graph using DFS is:")
print(g.topological_sort_dfs())
