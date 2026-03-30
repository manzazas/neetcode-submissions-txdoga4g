class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Traverse the island
        #store the max area
        #store the cur area of each island
        max_count = 0
        visited = set()
        neighbors = [[0,1], [0,-1],[-1,0],[1,0]]
        def dfs(r,c):
            if (r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == 0 or (r,c) in visited):
                return 0
            
            visited.add((r,c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))




        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] not in visited:
                    cur_count = 0
                    max_count = max(max_count,dfs(r,c))

        return max_count