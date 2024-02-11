class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def dp(leftRobot, rightRobot, row):
            if row == len(grid):
                return 0
            if leftRobot < 0:
                leftRobot = 0
            if rightRobot == len(grid[0]):
                rightRobot = len(grid[0]) - 1
            if leftRobot >= rightRobot:
                return -float("inf")
            return max([
                dp(leftRobot - 1, rightRobot - 1, row + 1),
                dp(leftRobot - 1, rightRobot, row + 1),
                dp(leftRobot - 1, rightRobot + 1, row + 1),
                dp(leftRobot, rightRobot - 1, row + 1),
                dp(leftRobot, rightRobot, row + 1),
                dp(leftRobot, rightRobot + 1, row + 1),
                dp(leftRobot + 1, rightRobot - 1, row + 1),
                dp(leftRobot + 1, rightRobot, row + 1),
                dp(leftRobot + 1, rightRobot + 1, row + 1),
            ]) + grid[row][leftRobot] + grid[row][rightRobot]

        return dp(0, len(grid[0])-1, 0)
