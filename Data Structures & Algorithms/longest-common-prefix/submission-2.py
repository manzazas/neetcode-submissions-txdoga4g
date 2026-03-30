class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_string = strs[0]
        for stringy in strs:
            if len(stringy) < len(min_string):
                min_string = stringy


        for i in range(0,len(min_string)):
            candidate = strs[0][i]
            for j in range(0,len(strs)):
                if strs[j][i] != candidate:
                    return prefix
            prefix = prefix + candidate

        return prefix

    


        
        