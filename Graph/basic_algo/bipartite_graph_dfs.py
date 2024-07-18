from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def is_bipartite_dfs(self):
        # Initialize colors for all vertices: -1 means uncolored, 0 and 1 are two different colors
        colors = [-1] * len(self.graph)
        
        # Check bipartiteness for all connected components
        for i in range(len(self.graph)):
            if colors[i] == -1:  # If vertex i is uncolored
                if not self.dfs_util(i, colors, 0):  # Start DFS from vertex i with color 0
                    return False
        return True
    
    def dfs_util(self, v, colors, color):
        colors[v] = color  # Assign current color to vertex v
        
        # Traverse all adjacent vertices
        for neighbor in self.graph[v]:
            if colors[neighbor] == -1:  # If neighbor is uncolored
                if not self.dfs_util(neighbor, colors, 1 - color):  # Recursively call DFS with opposite color
                    return False
            elif colors[neighbor] == color:  # If neighbor is colored with the same color as v
                return False
        
        return True

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)

if g.is_bipartite_dfs():
    print("Graph is bipartite")
else:
    print("Graph is not bipartite")
