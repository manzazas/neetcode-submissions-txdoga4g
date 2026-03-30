class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m,n = len(grid), len(grid[0])


        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"
                dfs(i + 1,j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)








        island_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r,c)


        return island_count
                
        