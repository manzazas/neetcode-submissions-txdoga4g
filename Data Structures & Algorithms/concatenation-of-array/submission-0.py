class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        for i in range(len(nums) * 2):
            if i < len(nums):
                ans.append(nums[i])
                count +=1
            if i>= len(nums):
                ans.append(nums[i % len(nums)])
        return ans
        