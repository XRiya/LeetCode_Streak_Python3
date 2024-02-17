class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap, n = [], len(heights)
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heappush(heap, diff) # use ladders
                # ladders are all in used, find the current shortest climb to use bricks instead
                if len(heap) > ladders:
                    bricks -= heappop(heap) # use bricks instead ladder
                    if bricks < 0:
                        return i
        return n-1
