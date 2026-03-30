from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #keep track of seen edges
        #We use dfs to find all other edges
        #whenever we call dfs in the main loop, we count + 1
        #if we dont call dfs again, that means every node was connected in the first place

        components = 0
        if edges == []:
            return n
        neighbors = defaultdict(list)
        for node1,node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)

        




        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in neighbors[node]:
                dfs(neighbor)

            return seen
            


        for i in range(0,n):
            if i not in seen:
                components += 1
                dfs(i)

        return components
            

        

            

        