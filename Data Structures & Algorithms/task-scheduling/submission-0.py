class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #X,X,Y,Y
        #X, Y , X, Y
        count = {}
        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1
        totals = list(count.values())
        heapq.heapify_max(totals)
        q = deque()
        time = 0
        while totals or q:
            if totals:
                cur = heapq.heappop_max(totals)
                time += 1
                if cur - 1 > 0:
                    q.append((cur - 1,time + n))
                while q and q[0][1] == time:
                    heapq.heappush_max(totals,q.popleft()[0])
            else:
                time += 1
                while q and q[0][1] == time:
                    heapq.heappush_max(totals,q.popleft()[0])
                
















        return time



