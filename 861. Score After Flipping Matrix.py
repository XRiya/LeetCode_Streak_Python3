class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 0:
                for j in range(len(row)):
                    if row[j] == 0: row[j] = 1
                    else: row[j] = 0
        length = len(grid[0])
        total = len(grid) * 2**(length-1)
        i = 1
        while i < length:
            j = 0
            ones = 0
            while j < len(grid):
                if grid[j][i] == 1: ones += 1
                j += 1
            total += 2**(length-1-i) * max(ones, len(grid) - ones)
            i += 1
        return total
