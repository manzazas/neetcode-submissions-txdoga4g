class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # min(1 + dfs(left), 1 + dfs(right)...)
        neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
        def bfs(q):
            seen = set()
            dist = 1
            while q: 
                for i in range(0,len(q)):  
                    cur = q.popleft()
                    seen.add(cur)
                    for nr,nc in neighbors:
                        newrow = nr + cur[0]
                        newcol = nc + cur[1]
                        if newrow < 0 or newcol < 0 or newrow >= len(grid) or newcol >= len(grid[0]) or (newrow,newcol) in seen or grid[newrow][newcol] == -1 or grid[newrow][newcol] == 0:
                            continue
                        else:
                            q.append((newrow,newcol))
                            grid[newrow][newcol] = min(grid[newrow][newcol], dist)
                            
                dist += 1
            


        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))

        bfs(q)
          


        