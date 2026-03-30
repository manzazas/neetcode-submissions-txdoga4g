class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_count = {}
        max_count = 0
        left = 0
        for right in range(len(s)):
            if s[right] in letter_count:
                letter_count[s[right]] += 1
            else:
                letter_count[s[right]] = 1
            while (right - left) + 1 - max(letter_count.values()) > k:
                letter_count[s[left]] -= 1
                left += 1

    

            max_count = max(max_count, (right - left) + 1)


        
        

        
        return max_count