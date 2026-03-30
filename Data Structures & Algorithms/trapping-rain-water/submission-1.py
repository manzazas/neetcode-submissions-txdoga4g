class Solution:
    def trap(self, height: List[int]) -> int:
        #2 pointers, left and right
        #right is one up goes until it reaches a non zero number. if there is an obstruction, count its height and subtract from total area
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        total = 0
        for i in range(0,len(height)):
            maxlen = 0
            for j in range(0,i):
                maxLeft[i] = max(maxLeft[i],height[j])
            for k in range(i + 1,len(height)):
                maxRight[i] = max(maxRight[i],height[k])
            area = min(maxLeft[i],maxRight[i]) - height[i]
            if area > 0:
                total += area
        return total

        