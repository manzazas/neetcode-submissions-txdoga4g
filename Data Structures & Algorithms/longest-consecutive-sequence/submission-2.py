class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashy = {}
        for num in nums:
            hashy[num] = 1
        max_count = 0

        for keys in hashy:
            if keys - 1 not in hashy:
                start = keys + 1
                count = 1
                
                while start in hashy:
                    count += 1
                    start = start + 1
                    
                max_count = max(count,max_count)
        return max_count

                
       

    


        