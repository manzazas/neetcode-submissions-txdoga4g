from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # allow negatives too
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                term2 = stack.pop()
                term1 = stack.pop()
                if token == '/':
                    # truncate toward 0 per LeetCode
                    stack.append(int(term1 / term2))
                else:
                    # keep using eval for +, -, *
                    stack.append(eval(str(term1) + token + str(term2)))
        return stack.pop()
