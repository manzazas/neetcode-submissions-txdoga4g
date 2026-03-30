class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_hashy = {}
        for letter in s:
            if letter not in s_hashy:
                s_hashy[letter] = 1
            else:
                s_hashy[letter] += 1
            
        for letter in t:
            if letter not in s_hashy:
                return False
            else:
                s_hashy[letter] += 1
        for val in s_hashy.values():
            if val % 2 != 0:
                return False
        return True
    