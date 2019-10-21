import heapq


# Solution 1: My own initial implementation.
class MedianFinder1:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.larger_half = []  # min heap
        self.smaller_half = []  # max heap
        heapq.heapify(self.larger_half)
        heapq.heapify(self.smaller_half)

    def addNum(self, num: int) -> None:
        if self.smaller_half and num <= -1 * self.smaller_half[0]:
            heapq.heappush(self.smaller_half, -1 * num)
        elif self.larger_half and num >= self.larger_half[0]:
            heapq.heappush(self.larger_half, num)
        else:
            # When a heap doesn't exist or number is between max of smaller
            # half and min of larger half, push onto larger_half heap.
            heapq.heappush(self.larger_half, num)

        # Balance heaps - so their size differs at most by 1
        if len(self.smaller_half) < len(self.larger_half):
            heapq.heappush(self.smaller_half, -1 * heapq.heappop(self.larger_half))
        elif len(self.larger_half) < len(self.smaller_half):
            heapq.heappush(self.larger_half, -1 * heapq.heappop(self.smaller_half))

    def findMedian(self) -> float:
        if len(self.larger_half) == len(self.smaller_half):
            return (self.larger_half[0] + -1 * self.smaller_half[0]) / 2
        else:
            if len(self.larger_half) < len(self.smaller_half):
                return -1 * self.smaller_half[0]
            else:
                return self.larger_half[0]


# Solution 2: EPI-based solution.
class MedianFinder2:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.larger_half = []  # min heap
        self.smaller_half = []  # max heap
        heapq.heapify(self.larger_half)
        heapq.heapify(self.smaller_half)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller_half, -1 * heapq.heappushpop(self.larger_half, num))

        # Balance heaps - so their size differs at most by 1
        if len(self.smaller_half) > len(self.larger_half):
            heapq.heappush(self.larger_half, -1 * heapq.heappop(self.smaller_half))

    def findMedian(self) -> float:
        if len(self.larger_half) == len(self.smaller_half):
            return (self.larger_half[0] + -1 * self.smaller_half[0]) / 2
        else:
            return self.larger_half[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
