from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        # Iterate through all the adjacent vertices
        for neighbor in self.graph[v]:
            # If the adjacent vertex is not visited, then recurse on it
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            # If an adjacent vertex is visited and not the parent of the current vertex, then there is a cycle
            elif parent != neighbor:
                return True
        
        return False
    
    def is_cyclic(self):
        visited = {i: False for i in self.graph}
        
        # Call the recursive helper function to detect cycle in different DFS trees
        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, -1):
                    return True
        
        return False

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)

if g.is_cyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
