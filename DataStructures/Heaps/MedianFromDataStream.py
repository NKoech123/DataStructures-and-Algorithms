from heapq import heappush,heappop

class MedianFinder:

    def __init__(self):
        self.lo = [] # max-heap:  to store the smaller half of the numbers.Allowed to store one more element
        self.hi = [] # min-headp: to store the larger half of numbers
      
    def addNum(self, num: int) -> None:
        
        '''
        Add num to max-heap lo. Since lo received a new element, we must do a balancing step
        for hi
        
        '''
        
        heappush(self.lo , -num)
        
        val = -1* heappop(self.lo)
        heappush(self.hi, val)
        
        if len(self.lo) < len(self.hi):
            val=-heappop(self.hi)
            heappush( self.lo , val )

    def findMedian(self) -> float:
        
        if len(self.lo) == len(self.hi):
            return ((-self.lo[0] + self.hi[0]))/2
        return -self.lo[0]
     
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
