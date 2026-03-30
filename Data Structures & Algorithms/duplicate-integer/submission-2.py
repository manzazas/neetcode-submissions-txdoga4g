class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numlist = set()
        for num in nums:
            if num in numlist:
                return True;
            else:
                numlist.add(num)

        return False
        