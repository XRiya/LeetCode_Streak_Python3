class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        
        n, keys, open = len(rooms), deque([0]), set()
        
        while keys and len(open) < n:
            key = keys.popleft()
            open.add(key)
            
            for r in rooms[key]:
                if r not in open:
                    keys.append(r)
                    
        return len(open) == n
