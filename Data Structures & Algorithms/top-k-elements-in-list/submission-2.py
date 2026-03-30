class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        max_values = []
        for i in range(0,k):
            cur_max = 0
            max_num = 0
            for number in freq:
                if freq[number] >= cur_max and number not in max_values:
                    cur_max = freq[number]
                    max_num = number
            max_values.append(max_num)

        return max_values

        