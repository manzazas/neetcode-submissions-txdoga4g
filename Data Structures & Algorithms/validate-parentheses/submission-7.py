class Solution:
    def isValid(self, s: str) -> bool:
        mappy = {")":"(", "}":"{", "]":"["}

        stacky = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stacky.append(char)
            elif stacky and (char ==  ")" or char == "]" or char == "}"):
                if stacky.pop() != mappy[char]:
                    return False
            else:
                return False

        if stacky:
            return False
        else:
            return True
        