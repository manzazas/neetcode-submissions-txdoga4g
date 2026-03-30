class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []
        heapq.heapify(self.upper)
        heapq.heapify_max(self.lower)
        

    def addNum(self, num: int) -> None:
        
        if self.upper and num > self.upper[0]:  
            heapq.heappush(self.upper,num)
        else:
            heapq.heappush_max(self.lower,num)
        if len(self.upper) > len(self.lower) + 1:
            heapq.heappush_max(self.lower,(heapq.heappop(self.upper)))
        elif len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper,(heapq.heappop_max(self.lower)))


        

        

    def findMedian(self) -> float:
        if len(self.upper) == len(self.lower):
            med1,med2 = self.lower[0], self.upper[0]
            return (med1 + med2) / 2
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
        else:
            return self.lower[0]
        
        