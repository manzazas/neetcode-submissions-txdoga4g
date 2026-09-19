class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxSize = 0

        def dfs(row,col):
            neighbors = [(row + 1,col), (row, col + 1), (row - 1,col), (row,col - 1)]
            seen.add((row,col))
            area = 1

            for neighbor in neighbors:
                if neighbor[0] >= 0 and neighbor[0] < len(grid) and neighbor[1] >= 0 and neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 1 and neighbor not in seen:
                    area += dfs(neighbor[0],neighbor[1])
            return area

        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in seen:
                    count = dfs(r,c)
                    maxSize = max(maxSize,count)   

        return maxSize