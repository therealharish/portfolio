class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = []
        for i in range(1, 1001):
            self.minHeap.append(i)
        heapify(self.minHeap)

    def popSmallest(self) -> int:
        return heappop(self.minHeap)

    def addBack(self, num: int) -> None:
        if num not in self.minHeap:
            heappush(self.minHeap, num)        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)