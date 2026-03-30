class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}

        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in hashy:
                return [hashy[diff], i]

            
            hashy[nums[i]] = i
            
            
