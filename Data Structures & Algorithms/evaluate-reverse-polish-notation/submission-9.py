class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacky = []
        for item in tokens:
            if item == "+" or item == "-" or item == "/" or item == "*":
                operand2 = stacky.pop()
                operand1 = stacky.pop()
                if item == "+":
                    result = int(operand1) + int(operand2)
                if item == "-":
                    result = int(operand1) - int(operand2)
                if item == "/":
                    result = int(operand1) / int(operand2)
                if item == "*":
                    result = int(operand1) * int(operand2)
                stacky.append(result)
            else:
                stacky.append(int(item))


        return int(stacky[-1])
            



        