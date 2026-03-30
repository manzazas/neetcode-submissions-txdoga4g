class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        for i in range(0,k):
            final = heapq.heappop_max(nums)


        return final
        
        