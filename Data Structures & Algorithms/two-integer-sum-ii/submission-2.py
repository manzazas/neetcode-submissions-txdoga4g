class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Store numbers as we go in a hashmap
        #Find difference of target-currentvalie
        #return in index1 < index2 order
        #make sure they are not equal

        num_map = {}
        for i in range(0,len(numbers)):
            difference = target - numbers[i]
            if difference in num_map:
                return [num_map[difference] + 1,i + 1]
            else:
                num_map[numbers[i]] = i

        return -1 

        