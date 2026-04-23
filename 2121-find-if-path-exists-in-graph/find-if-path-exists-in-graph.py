from collections import deque

class Solution(object):
    def validPath(self, n, edges, source, destination):
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)   # undirected graph
        
        # Step 2: BFS
        visited = set()
        queue = deque([source])
        
        while queue:
            node = queue.popleft()
            
            if node == destination:
                return True
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for neighbor in graph[node]:
                queue.append(neighbor)
        
        return False