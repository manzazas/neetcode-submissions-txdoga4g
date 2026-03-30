class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        res = set()
        l = 0

        for r in range(0,len(nums)):
            if ((r - l) > k):
                res.remove(nums[l])
                l += 1
            
            if nums[r] in res:
                return True
            else:
                res.add(nums[r])

        return False

            
        