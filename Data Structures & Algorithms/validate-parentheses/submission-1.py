class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hashy = {")":"(","]":"[","}":"{"}
    
        for char in s:
            if char in hashy.values():
                stack.append(char)
            elif stack and hashy[char] == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
            


