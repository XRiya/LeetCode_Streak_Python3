# Time: O(mn)
class Solution:
		def islandPerimeter(self, grid: List[List[int]]) -> int:
			isLands = 0
			nghbrs = 0
			grd_len = len(grid)
			grd0_len = len(grid[0])
			for i in range(grd_len):
				for j in range(grd0_len):
					if grid[i][j] == 1:
						isLands += 1
						if i < grd_len-1 and grid[i+1][j] == 1:
							nghbrs += 1  # Counting next Down Neighbour...
						if j < grd0_len-1 and grid[i][j+1] == 1:
							nghbrs += 1  # Counting next Right Neighbour...
			return 4*isLands - 2*nghbrs
