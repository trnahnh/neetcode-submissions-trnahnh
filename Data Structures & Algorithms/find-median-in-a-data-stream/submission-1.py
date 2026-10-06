class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if len(self.upper) > 0 and num > self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -1 * num)
        
        if len(self.lower) > len(self.upper) + 1:
            val = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)
        elif len(self.upper) > len(self.lower):
            val = -1 * heapq.heappop(self.upper)
            heapq.heappush(self.lower, val)

    def findMedian(self) -> float:
        median = -1 * self.lower[0]
        if len(self.lower) > len(self.upper):
            return median
        else:
            return (median + self.upper[0]) / 2