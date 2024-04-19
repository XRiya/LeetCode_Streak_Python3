class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m=len(grid), len(grid[0])
        def inside(i, j):
            return 0<=i and i<n and 0<=j and j<m
        def dfs(i, j):
            if not inside(i, j): return
            if grid[i][j]=='1':
                grid[i][j]='2'
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
        num=0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x=='1':
                    num+=1
                    dfs(i, j)
        return num
