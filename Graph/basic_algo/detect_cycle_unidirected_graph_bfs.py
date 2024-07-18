from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def is_cyclic_bfs(self, start, visited):
        # Create a queue for BFS
        queue = deque([(start, -1)])  # (current_node, parent_node)
        
        # Mark the starting node as visited
        visited[start] = True
        
        while queue:
            current_node, parent_node = queue.popleft()
            
            # Traverse all the adjacent vertices
            for neighbor in self.graph[current_node]:
                # If the adjacent vertex is not visited, mark it visited and enqueue it
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, current_node))
                # If the adjacent vertex is visited and is not the parent, then there is a cycle
                elif neighbor != parent_node:
                    return True
        
        return False
    
    def is_cyclic(self):
        visited = {i: False for i in self.graph}
        
        # Check for cycle in different BFS trees
        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_bfs(node, visited):
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
