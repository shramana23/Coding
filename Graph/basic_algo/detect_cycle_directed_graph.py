from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[v] = False
        return False
    
    def is_cyclic(self):
        visited = [False] * len(self.graph)
        rec_stack = [False] * len(self.graph)
        
        for node in range(len(self.graph)):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        
        return False

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

if g.is_cyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
