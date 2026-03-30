class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        letters_seen = []
        max_length = 0

        for char in s:
            if char in letters_seen:
                max_length = max(max_length, len(letters_seen))
                index_remove = letters_seen.index(char)
                letters_seen = letters_seen[index_remove + 1:]
            letters_seen.append(char)
        max_length = max(max_length, len(letters_seen))
        return max_length
