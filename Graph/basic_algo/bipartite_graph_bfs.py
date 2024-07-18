from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def is_bipartite_bfs(self):
        colors = [-1] * len(self.graph)  # Initialize colors for all vertices: -1 means uncolored, 0 and 1 are two different colors
        
        for i in range(len(self.graph)):
            if colors[i] == -1:  # If vertex i is uncolored
                if not self.bfs_util(i, colors):  # Start BFS from vertex i
                    return False
        return True
    
    def bfs_util(self, start, colors):
        queue = deque([start])  # Initialize queue for BFS
        colors[start] = 0  # Color the starting vertex with color 0
        
        while queue:
            current_node = queue.popleft()
            current_color = colors[current_node]
            
            for neighbor in self.graph[current_node]:
                if colors[neighbor] == -1:  # If neighbor is uncolored
                    colors[neighbor] = 1 - current_color  # Assign opposite color to neighbor
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:  # If neighbor has the same color as current node
                    return False
        
        return True

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)

if g.is_bipartite_bfs():
    print("Graph is bipartite")
else:
    print("Graph is not bipartite")
