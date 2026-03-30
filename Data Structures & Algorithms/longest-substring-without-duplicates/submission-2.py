class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        letters_seen = set()
        l = 0
        max_length = 0


        for r in range(0,len(s)):
            while s[r] in letters_seen:
                letters_seen.remove(s[l])
                l += 1
            letters_seen.add(s[r])
            max_length = max(r - l + 1, max_length)

        return max_length




     
