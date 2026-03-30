class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #dfs 
        #we check each neighbor, if the neighbor is out of bounds or 0, it is water and we add 1
        #if it is an island, we check its borders and dfs 
        seen = set()
        
        def dfs(row,col):
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0 or grid[row][col] == 0:
                return 1

            if (row,col) in seen:
                return 0
            seen.add((row,col))
            perimeter = dfs(row + 1, col)
            perimeter += dfs(row,col + 1)
            perimeter += dfs(row - 1,col)
            perimeter += dfs(row,col - 1)
            return perimeter


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in seen:
                    return dfs(r,c)

           


        