class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        return self.minFallingPathSumHelper(0, grid).minSum
    
    def minFallingPathSumHelper(self, row: int, grid: List[List[int]]) -> 'Triplet':
        if row == len(grid):
            return Triplet(0, 0, 0)

        next_row_triplet = self.minFallingPathSumHelper(row + 1, grid)
        current_triplet = Triplet(float('inf'), float('inf'), -1)

        for col in range(len(grid[0])):
            value = grid[row][col] + (
                next_row_triplet.minSum if col != next_row_triplet.minSumIndex else next_row_triplet.secondMinSum
            )
            if value <= current_triplet.minSum:
                current_triplet.secondMinSum = current_triplet.minSum
                current_triplet.minSum = value
                current_triplet.minSumIndex = col
            elif value < current_triplet.secondMinSum:
                current_triplet.secondMinSum = value

        return current_triplet

class Triplet:
    def __init__(self, minSum: int, secondMinSum: int, minSumIndex: int):
        self.minSum = minSum
        self.secondMinSum = secondMinSum
        self.minSumIndex = minSumIndex
