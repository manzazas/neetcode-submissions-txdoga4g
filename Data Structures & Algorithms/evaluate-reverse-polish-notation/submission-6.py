class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                term2 = stack.pop()
                term1 = stack.pop()
                stack.append(term1 - term2)
            elif token =="*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                term2 = stack.pop()
                term1 = stack.pop()
                stack.append(int(term1 / term2))
            else:
                stack.append(int(token))

        return stack.pop()
        




        