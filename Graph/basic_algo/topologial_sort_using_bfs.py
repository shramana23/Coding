from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1
    
    def topological_sort_kahn(self):
        # Step 1: Compute in-degree for each vertex
        for v in self.graph:
            for u in self.graph[v]:
                self.in_degree[u] += 1
        
        # Step 2: Initialize a queue with vertices with in-degree 0
        queue = deque([v for v in self.graph if self.in_degree[v] == 0])
        topological_order = []
        
        # Step 3: Process the queue
        while queue:
            v = queue.popleft()
            topological_order.append(v)
            
            # Decrease the in-degree of all adjacent vertices
            for u in self.graph[v]:
                self.in_degree[u] -= 1
                # If in-degree of a vertex becomes 0, enqueue it
                if self.in_degree[u] == 0:
                    queue.append(u)
        
        # Step 4: Check for cycle (if not all vertices are added)
        if len(topological_order) != len(self.graph):
            raise ValueError("Graph contains a cycle")
        
        return topological_order

# Example usage
g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

try:
    print("Topological Sort of the given graph using Kahn's Algorithm is:")
    print(g.topological_sort_kahn())
except ValueError as e:
    print(e)
