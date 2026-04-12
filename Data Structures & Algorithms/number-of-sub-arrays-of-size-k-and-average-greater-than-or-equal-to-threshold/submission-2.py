class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #static window of size k
        #keep track of the total of each window
        #divide total by k, check if >= threshold

        l = 0
        r = 0
        total = 0
        res = 0
        while r < k:
            total += arr[r]
            r += 1
        while r < len(arr):
            if (total / k) >= threshold:
                res += 1
            total -= arr[l]
            l += 1
            total += arr[r]
            r += 1



        if (total / k) >= threshold:
                res += 1
        return res
            

        