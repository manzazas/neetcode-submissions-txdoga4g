class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stacky = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            
            while stacky and stacky[-1][0] < temp:
                prevTempIndex = stacky.pop()
                res[prevTempIndex[1]] = i - prevTempIndex[1]
            stacky.append([temp,i])


        return res

        