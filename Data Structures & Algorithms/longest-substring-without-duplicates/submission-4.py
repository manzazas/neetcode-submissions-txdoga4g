class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        cur_len = 0
        l = 0
        r = 0
        freq = {}
        while r < len(s):
            if s[r] not in freq:
                freq[s[r]] = 1
                cur_len += 1
                r += 1

            else:
                max_len = max(max_len,cur_len)
                
                while s[r] in freq:
                    del freq[s[l]]
                    l += 1
                    cur_len -= 1


                
    
        return max(max_len,cur_len)


        
