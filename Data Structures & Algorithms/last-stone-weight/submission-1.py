class Solution:
    #[1,2,3,4,5] [-1,-2,-3,-4,-5]
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heapify the list
        #find the two biggest numbers x,y
        #if x = y, pop both
        #else, subtract the bigger one by the smaller one and remove the smaller one
        #i.e. x = 6, y = 4, change x to 2 and remove the 4
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x > y:
                heapq.heappush(max_heap,-(x-y))

        return abs(max_heap[0]) if max_heap else 0

                
