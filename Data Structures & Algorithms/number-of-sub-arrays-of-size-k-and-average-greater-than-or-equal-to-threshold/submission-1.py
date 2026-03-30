class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        res = 0
        cur = 0
        

        l = 0
        for r in range(0,len(arr)):
            cur += arr[r]
            if (r - l) >= k:
                cur -= arr[l]
                l += 1
            if (r - l) == (k - 1) and (cur / k) >= threshold:
                res += 1
            

        return res

            



        


        