class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #from each treasure chest, do a BFS
        #At each round, put in the square the number of the round
        #Do not override if the current round is more than whats on the square
        def bfs(queue):
            visited = set()
            while queue:
                
                coord = queue.popleft()
                neighbors = [(coord[0] + 1, coord[1]), (coord[0], coord[1] + 1), (coord[0]- 1, coord[1]), (coord[0], coord[1] - 1)]
                visited.add((coord[0],coord[1]))
                for neighbor in neighbors:
                    if neighbor[0] >= 0 and neighbor[0] < len(grid) and neighbor[1] >= 0 and neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != -1 and (neighbor[0],neighbor[1]) not in visited:
                        grid[neighbor[0]][neighbor[1]] = min(grid[coord[0]][coord[1]] + 1, grid[neighbor[0]][neighbor[1]])
                        queue.append((neighbor[0],neighbor[1]))
                        visited.add((neighbor[0],neighbor[1]))
                    





        queue = deque()
        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c))

        bfs(queue)
        
    
     
        
            
        