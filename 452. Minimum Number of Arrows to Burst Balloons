class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        x, y = points[0]
        res = 0
        for i in range(1, n):
            x1, y1 = points[i]
            if x <= x1 <= y:
                x = max(x, x1)
                y = min(y, y1)
            else:
                res += 1
                x, y = x1, y1
        return res + 1
