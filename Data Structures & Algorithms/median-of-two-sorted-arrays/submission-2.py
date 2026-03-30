class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = nums1
        list2 = nums2
        if len(list2) < len(list1):
            list1,list2 = list2,list1
        total = len(list1) + len(list2)
        half = total // 2

        l = 0
        r = len(list1) - 1
        while True:
            LsideA = (l + r) // 2
            LsideB = half - LsideA - 2
            Aleft = list1[LsideA] if LsideA >= 0 else float("-infinity")
            Aright = list1[LsideA + 1] if LsideA + 1 < len(list1) else float("infinity")
            Bleft = list2[LsideB] if LsideB >= 0 else float("-infinity")
            Bright = list2[LsideB + 1] if LsideB + 1 <len(list2) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    #if even
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
                else: 
                    #if odd
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = LsideA - 1
            else:
                l = LsideA + 1




            




