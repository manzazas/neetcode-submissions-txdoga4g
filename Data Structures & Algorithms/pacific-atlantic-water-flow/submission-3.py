class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        #core algorithm: at each border cell, bfs upwards and add those cells to the starting cell's border
        #first, add the border cells to their sets

        def bfs(row,col,startType):
            queue = deque()
            visited = set()
            visited.add((row,col))
            queue.append((row,col))

            while queue:
                r,c = queue.popleft()
                neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for nr,nc in neighbors:
                    if nr >= 0 and nr < len(heights) and nc >= 0 and nc < len(heights[0]) and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        if startType == "both":
                            pacific.add((nr,nc))
                            atlantic.add((nr,nc))
                        elif startType == "pacific":
                            pacific.add((nr,nc))
                        elif startType == "atlantic":
                            atlantic.add((nr,nc))

                        
        for r in range(0,len(heights)):
            for c in range(0,len(heights[0])):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    atlantic.add((r,c))
        for r in range(0,len(heights)):
            for c in range(0,len(heights[0])):
                if (r == 0 or c == 0) and (r == len(heights) - 1 or c == len(heights[0]) - 1):
                    startType = "both"
                    bfs(r,c,startType)
                if r == len(heights) - 1 or c == (len(heights[0]) - 1):
                    startType = "atlantic"
                    bfs(r,c,startType)
                if (r == 0 or c == 0):
                    startType = "pacific"
                    bfs(r,c,startType)
        res = []
        for r in range(0,len(heights)):
            for c in range(0,len(heights[0])):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
        
        

            



        