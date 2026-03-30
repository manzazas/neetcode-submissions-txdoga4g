class Solution:
    def isValid(self, s: str) -> bool:
        ops = []
        for i in range(0,len(s)):
            if s[i] == "}":
                if not ops or ops[-1] != "{":
                    return False
                else:
                    ops.pop()
            elif s[i] == ")":
                if not ops or ops[-1] != "(":
                    return False
                else:
                    ops.pop()
            elif s[i] == "]":
                if not ops or ops[-1] != "[":
                    return False
                else:
                    ops.pop()
            else:
                ops.append(s[i])

        if not ops:
            return True
        else:
            return False
        