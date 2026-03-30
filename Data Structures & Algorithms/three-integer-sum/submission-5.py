class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()


        for i,value in enumerate(nums):
            if i > 0 and value == nums[i - 1]:
                continue
            target = 0 - value
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[right] + nums[left] < target:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1


        return res
                    
                