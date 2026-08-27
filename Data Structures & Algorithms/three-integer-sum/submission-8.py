class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valids = []
        nums.sort()
        def twosum(target, start):
            hash = {}
            for i in range(start,len(nums)):
                if nums[i] in hash:
                    tuplit = [-target, hash[nums[i]], nums[i]]
                    if tuplit not in valids:
                        valids.append(tuplit)
        
                hash[target - nums[i]] = nums[i]
        for i in range(0,len(nums) - 2):
            twosum(-nums[i], i + 1)

        return valids


        # sorting: nlogn
        # outer loop: n
        # inner loop: n
