class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0] #range is 0-2 so 3 possible elements

        for num in nums:
            count[num] += 1
        #[1,2,1]
        index = 0
        for i in range(0,len(count)):
            for j in range(0,count[i]):
                nums[index] = i
                index += 1
        return nums

        