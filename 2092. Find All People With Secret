class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)

        for person1, person2, time in meetings:
            graph[person1].append((person2, time))
            graph[person2].append((person1, time))
        
        earliest = [maxsize if i != 0 and i != firstPerson else 0 for i in range(n)]

        queue = deque([(0, 0), (firstPerson, 0)])

        while queue:
            person, time = queue.popleft()

            for nxt, t in graph[person]:
                if t >= time and earliest[nxt] > t:
                    earliest[nxt] = t
                    queue.append((nxt, t))
        
        return [i for i, x in enumerate(earliest) if x != maxsize]
