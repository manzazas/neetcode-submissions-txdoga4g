class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #we have a set for atlantic and pacfiic.
        #if neighbor can visit atlantic
        #res list shows cooridnates that can visit both


        res = []
        seen = set()
        pacific = set()
        atlantic = set()
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        #down, up, right, left


        def pacificdfs(row,col):
            pacific.add((row,col))
            for nr,nc in neighbors:
                if (row + nr) < 0 or row + nr == len(heights) or col + nc < 0 or col + nc == len(heights[0]) or (row + nr,col + nc) in pacific or heights[row][col] > heights[row + nr][col + nc]:
                    continue
                else:
                    
                    pacificdfs(row + nr,col + nc)
        
        def atlanticdfs(row,col):
            atlantic.add((row,col))
            for nr,nc in neighbors:
                if row + nr < 0 or row + nr == len(heights) or col + nc < 0 or col + nc == len(heights[0]) or (row + nr,col + nc) in atlantic or heights[row][col] > heights[row + nr][col + nc]:
                    continue
                else:
                    atlanticdfs(row + nr, col + nc)
            

                

            

                
        for r in range(0,len(heights)):
            for c in range(0,len(heights[0])):
                if r == 0 or c == 0:
                    pacificdfs(r,c)
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    atlanticdfs(r,c)


        #unionize atlatnic and pacific lists

        return list(atlantic & pacific)


        
                