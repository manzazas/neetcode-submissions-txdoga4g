class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        l = 0
        res = 0


        for r in range(0,len(s)):
            if s[r] in count:
                count[s[r]] = count[s[r]] + 1
            else:
                count[s[r]] = 0
            max_freq = max(max_freq,count[s[r]])

            while (r - l - max_freq) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r -  l+ 1)


        return res
                

            
        




    
        








        