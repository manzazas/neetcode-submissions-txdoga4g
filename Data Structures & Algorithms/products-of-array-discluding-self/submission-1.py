class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        case1: no zeroes, just find total product and divide the nums[i]
        case2: 1 zero, only the index with the zero absorbs the total product
        case3: >1 zero, always zero

        """

        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1

        if zero_count == 0:
            total = 1
            output = [0] * (len(nums) )
            for num in nums:
                total = total * num
            for i in range(0,len(nums)):
                output[i] = int(total / nums[i])

            return output
            



        elif zero_count == 1:
            total = 1
            output = [0] * (len(nums))
            for num in nums:
                if num != 0:
                    total = total * num
            for i in range(0,len(nums)):
                if nums[i] == 0:
                    output[i] = total

            return output


        else:
            output = [0] * (len(nums))
            return output






        