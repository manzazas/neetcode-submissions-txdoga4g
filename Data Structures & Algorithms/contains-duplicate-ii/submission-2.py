class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 1
        numset = set()
        numset.add(nums[l])
        

        while r < k:
            if nums[r] == nums[l]:
                return True
            else:
                numset.add(nums[r])
                r += 1
            
        while r < len(nums):
            if nums[r] in numset:
                return True
            else:
                numset.remove(nums[l])
                l += 1
                numset.add(nums[r])
                r += 1

        return False




        