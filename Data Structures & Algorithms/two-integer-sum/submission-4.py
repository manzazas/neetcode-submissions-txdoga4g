class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_sum ={}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in target_sum:
                return [target_sum[diff],i]
            else:
                target_sum[nums[i]] = i
            

        
        