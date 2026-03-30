class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1 
        #{1:2, 6:1, 5:4}
        heap = []
        for num in count.keys():
            heapq.heappush(heap, [count[num], num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



