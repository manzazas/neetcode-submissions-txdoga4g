class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums) * 2):
            if i < len(nums):
                ans.append(nums[i])
                
            if i>= len(nums):
                ans.append(nums[i % len(nums)])
        return ans
        