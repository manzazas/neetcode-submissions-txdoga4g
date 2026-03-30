class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        self.graph[src].add(dst)



    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False
        else:
            self.graph[src].remove(dst)
            return True



    def hasPath(self, src: int, dst: int) -> bool:

        def dfs(self, src:int, dst: int, visited: set) -> bool:
            visited.add(src)
            q = deque([src])
            while queue:
                cur = q.popleft()
                if cur == dst:
                    return True
                
                # visited.add(cur)
                for neighbor in self.graph.get(curr,[]):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            return False
            
            
            
            
            # if src == dst:
            #     return True
            # visited.add(src)
            # for neighbor in self.graph.get(src,[]):
            #     if neighbor not in visited:
            #         if self.dfs(neighbor, dst, visited):
            #             return True
            # return False
        


        visited = set()
        return self.dfs(src,dst,visited)
    def dfs(self, src:int, dst: int, visited: set) -> bool:
            if src == dst:
                return True
            visited.add(src)
            for neighbor in self.graph.get(src,[]):
                if neighbor not in visited:
                    if self.dfs(neighbor, dst, visited):
                        return True
            return False
        











