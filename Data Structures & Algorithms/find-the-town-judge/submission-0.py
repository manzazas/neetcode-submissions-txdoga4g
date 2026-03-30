class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #create the adjency list
        #we loop through each 

        seen = set()
        trust_map = defaultdict(list)
        for first,second in trust:
            seen.add(first)
            if second in trust_map:
                trust_map[second].append(first)
            else:
                trust_map[second] = [first]

        if len(seen) == n:
            return -1
        
        #3:1,2,4
        #3:1,2 1:3, 2:3
        for key in trust_map:
            if len(trust_map[key]) == n - 1:
                return key
        return -1

        

            
