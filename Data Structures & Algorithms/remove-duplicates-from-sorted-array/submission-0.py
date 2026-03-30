class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # create a dictionary to store seen values
        # turn every duplicate to a common value, like 0
        # shift the zeros to the end

        dicti = {}
        uniqueCounter = 0
        for i in range(len(nums)):
            if nums[i] not in dicti.keys():
                dicti[nums[i]] = 1
                uniqueCounter +=1
            else:
                nums[i] = 101
        nums.sort()
        return uniqueCounter

        

        