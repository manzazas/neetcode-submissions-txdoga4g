class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for char in s1:
            if char in s1_map:
                s1_map[char] += 1
            else:
                s1_map[char] = 1
        #{a:1, b:1, c:1}

        s2_map = {}
        l = 0
        for r in range(0,len(s2)): 
            if s2[r] in s2_map:
                    s2_map[s2[r]] += 1
            else:
                s2_map[s2[r]] = 1

            if (r + 1 - l) == len(s1):
                if s1_map == s2_map:
                    return True
                else:
                    if s2_map[s2[l]] > 1:
                        s2_map[s2[l]] -= 1
                    else:
                        del s2_map[s2[l]]
                    l += 1
            
               
        return False
            



        
                


        