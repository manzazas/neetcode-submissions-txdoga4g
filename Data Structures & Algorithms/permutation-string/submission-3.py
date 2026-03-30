class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #fixed window of size len(s1)
        #store the window in a hashmap, check if its equal to the s1 hashmap
        #if not, delete the left char from the hashmap and move the right and left foward

        if len(s1) > len(s2):
            return False

        left = 0
        s1_map = {}
        s2_map = {}
        for char in s1:
            s1_map[char] = 1 + s1_map.get(char, 0)
        
        for right in range(0,len(s1)):
            s2_map[s2[right]] = 1 + s2_map.get(s2[right], 0)
        if s2_map == s1_map:
            return True

        for right in range(len(s1),len(s2)):
            if s2_map[s2[left]] > 1:
                s2_map[s2[left]] -= 1
            else:
                del s2_map[s2[left]]
            left += 1
            
            s2_map[s2[right]] = 1 + s2_map.get(s2[right], 0)

            if s1_map == s2_map:
                return True

            
           
           
        
        return False
        


            
                


        