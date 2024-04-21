from collections import defaultdict, deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create an adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize a visited set to keep track of visited vertices during traversal
        visited = set()
        
        # BFS traversal to find a path from source to destination
        queue = deque([source])
        while queue:
            curr_vertex = queue.popleft()
            if curr_vertex == destination:
                return True  # Path found
            visited.add(curr_vertex)
            for neighbor in graph[curr_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return False  # No path found
