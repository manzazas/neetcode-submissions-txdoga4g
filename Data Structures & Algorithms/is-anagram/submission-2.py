class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hashy,t_hashy = {}, {}
        for i in range(0,len(s)):
            s_hashy[s[i]] = 1 + s_hashy.get(s[i],0)
            t_hashy[t[i]] = 1 + t_hashy.get(t[i],0)

        return s_hashy == t_hashy

            
