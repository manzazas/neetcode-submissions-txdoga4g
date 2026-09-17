class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seen = set()
        
        def dfs(row,col):
            seen.add((row,col))
            neighbors = [(row + 1,col), (row, col + 1), (row - 1, col), (row, col - 1)]
            for neighbor in neighbors:
                if int(neighbor[0]) >= 0 and int(neighbor[0]) < len(grid) and int(neighbor[1]) >= 0 and int(neighbor[1]) < len(grid[0]) and str(grid[neighbor[0]][neighbor[1]]) == '1' and neighbor not in seen:
                    dfs(neighbor[0],neighbor[1])

            




        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in seen:
                    count+=1
                    dfs(r,c)
            
        return count
        

        
        