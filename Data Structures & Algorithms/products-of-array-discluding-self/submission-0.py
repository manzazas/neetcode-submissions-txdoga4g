class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Create a list the size of nums filled with the total
        #For each index in output, subtract nums[i]
        product = 1

        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product *= n
        output = []
        if zero_count > 1:
            return [0] * len(nums)
        
        elif zero_count == 1:
            for i in range(0,len(nums)):
                if nums[i] == 0:
                    output.append(product)
                else:
                    output.append(0)

        else:
             for i in range(0,len(nums)):
                output.append(int(product / nums[i]))

        return output
