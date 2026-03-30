class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #store visited elements in the hash
        #check if that element - 1 is in the hash


        numset = set(nums)
        
        #{100,4,200,1,3,2}
      



        max_length = 0
        for num in numset:
            if (num - 1) not in numset:
                starter = num
                sequence_length = 1
                starter += 1
                while starter in numset:
                    sequence_length += 1
                    starter += 1
                max_length = max(max_length,sequence_length)
            

        return max_length
            




    


        