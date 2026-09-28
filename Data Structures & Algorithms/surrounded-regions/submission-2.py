class Solution:
    def solve(self, board: List[List[str]]) -> None:

        Globalvisited = set()
        def bfs(row,col):
            #at the end of BFS, swap each cell if needed
            queue = deque()
            seen = set()
            tag = True
            queue.append((row,col))
            seen.add((row,col))
            Globalvisited.add((row,col))
            if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                            tag = False
            while queue:
                r,c = queue.popleft()
                neighbors = [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]
                for nr,nc in neighbors:
                    if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and board[nr][nc] == "O" and (nr,nc) not in seen:
                        if nr == 0 or nr == len(board) - 1 or nc == 0 or nc == len(board[0]) - 1:
                            tag = False
                        seen.add((nr,nc))
                        queue.append((nr,nc))
                        Globalvisited.add((nr,nc))
            if tag == True:
                for r,c in seen:
                    board[r][c] = "X"


            
        
        for r in range(0,len(board)):
            for c in range(0,len(board[0])):
                if board[r][c] == "O" and (r,c) not in Globalvisited:
                    bfs(r,c)
        
        