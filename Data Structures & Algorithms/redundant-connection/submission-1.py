class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)


        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]


        def union(a,b):
            pa,pb = find(a), find(b)

            if pa == pb:
                return False
            
            if rank[pa] > rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]

            return True




        for a,b in edges:
            if not union(a,b):
                return [a,b]





