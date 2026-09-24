class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        count = 0
        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r,c))
    
        while rotten:
            somethingRotted = False
            for i in range(0,len(rotten)):
                row,col = rotten.popleft()
                neighbors = [(row + 1,col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for neighbor in neighbors:
                    if neighbor[0] >= 0 and neighbor[0] < len(grid) and neighbor[1] >= 0 and neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 1:
                        grid[neighbor[0]][neighbor[1]] = 2
                        somethingRotted = True
                        rotten.append((neighbor[0],neighbor[1]))
            if somethingRotted:
                count += 1
            

        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return count
        
            
        
        