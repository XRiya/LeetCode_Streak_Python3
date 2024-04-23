class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, return the root

        # Build graph using adjacency list
        graph = defaultdict(list)
        degrees = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        # Initialize queue with leaf nodes (degree == 1)
        queue = deque()
        for i in range(n):
            if degrees[i] == 1:
                queue.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            # Remove current leaf nodes
            size = len(queue)
            remaining_nodes -= size
            
            for _ in range(size):
                leaf = queue.popleft()
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        
        return list(queue)
