class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # 0:1, 1:0,2,4 2:1,3 3: 1,2 4:1
        neighbors = defaultdict(list)
        if len(edges) != n - 1:
            return False

        for one,two in edges:
            neighbors[one].append(two)
            neighbors[two].append(one)

        

        seen = set()
        def dfs(prev,node):
            seen.add(node)
            for neighbor in neighbors[node]:
                if neighbor == prev:
                    continue
                elif neighbor in seen:
                    return False
            
                else:
                    if not dfs(node,neighbor):
                        return False
            return True

        
    
        return dfs(0,0) and len(seen) == n
        