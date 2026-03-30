class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stacky = []
        res = [0] * len(heights)
        for i,height in enumerate(heights):
            if not stacky or height >= stacky[-1][0]:
                stacky.append((height,i))
            else:
                back = i
                while stacky and stacky[-1][0] > height:
                    popped = stacky.pop()
                    area = popped[0] * (i - popped[1])
                    res[popped[1]] = max(res[popped[1]], area)
                    back = popped[1]
                
            
                stacky.append((height,back))

        if stacky:
            while stacky:
                popped = stacky.pop()
                area = popped[0] * (len(heights) - popped[1])
                res[popped[1]] = max(res[popped[1]], area)

        return max(res) if res else 0