class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        a1 = intervals[0][0]
        a2 = intervals[0][1]
        for first,second in intervals:
            if first <= a2:
                cur = [a1,max(second,a2)]
                a1 = cur[0]
                a2  = cur[1]
            else:
                res.append([a1,a2])
                a1 = first
                a2 = second
        res.append([a1,a2])
        return res









        return res

        