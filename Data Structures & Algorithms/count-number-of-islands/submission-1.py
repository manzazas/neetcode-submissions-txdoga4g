class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        seen = set()
        count = 0
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(row,col):
            seen.add((row,col))
            for nr,nc in neighbors:
                newrow = row + nr
                newcol = col + nc
                if newrow < 0 or newcol < 0  or newrow >= len(grid) or newcol >= len(grid[0]) or (newrow,newcol) in seen or grid[newrow][newcol] == "0":
                    continue
                else:
                    dfs(newrow,newcol)
            


        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if (r,c) not in seen and grid[r][c] == "1":
                    count += 1
                    dfs(r,c)

        return count