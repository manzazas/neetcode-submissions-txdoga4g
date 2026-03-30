class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #add the first rotten to a queue
        #store its neighbors in a queue
        #then go through the neighbors
        time, fresh = 0,0  
        q = collections.deque()
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] ==1:
                    fresh += 1
                if grid[m][n] == 2:
                    q.append([m,n])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        while q and fresh > 0:
            
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append([row,col]) 
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1





        

