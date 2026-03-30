class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Traverse the island
        #store the max area
        #store the cur area of each island
        q = deque()
        seen = set()
        max_area = 0
        neighbors =[(0,1),(1,0),(-1,0),(0,-1)]
        def bfs(row,col):
            count = 0
            seen.add((row,col))
            q.append((row,col))
            while q:
                current = q.popleft()
                count += 1
                for nr,nc in neighbors:
                    newrow = current[0] + nr
                    newcol = current[1] + nc
                    if newrow < 0 or newcol < 0 or newrow >= len(grid) or newcol >= len(grid[0]) or (newrow,newcol) in seen or grid[newrow][newcol] != 1:
                        continue
                    else:
                        q.append((newrow,newcol))
                        seen.add((newrow,newcol))

            return count


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in seen:
                    max_area = max(max_area,bfs(r,c))

        return max_area

            

