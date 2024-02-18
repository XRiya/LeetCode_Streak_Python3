class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # sort meetings
        meetings.sort()
        
        available = [i for i in range(n)]               # heap to store available rooms
        used = []                                       # used will store end time and used room number in pairs (end, room)
        counter = [0] * n                               # counter will store counter to count which room is used how many times
        
        # loop through the meetings
        for start, end in meetings:
            # used is not empty and current start value is greater or eq to lowest end time in used heap
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)           # pop from used
                heapq.heappush(available, room)         # push room in available heap
            

            # now check if all the rooms are used or not:
            if not available:
                endtime, room = heapq.heappop(used)     # pop from used
                end = endtime + (end-start)             # update the end time for current meeting
                heapq.heappush(available, room)         # push room back in available heap

            room = heapq.heappop(available)             # pop from availabe heap
            heapq.heappush(used, (end, room))           # push end, room in used heap
            counter[room] += 1                          # increment the room counter

        # once we are done with meeting we return the (room)index of max value in counter
        return counter.index(max(counter))
