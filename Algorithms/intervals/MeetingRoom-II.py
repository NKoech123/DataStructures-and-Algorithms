import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
       0.........................30
          5..10         15..20
        
        0......3
                  4.....5
             
             
        minHeap =[3,5]
        
        start >= minHeap[0]: pop the minHeap since a meeting ended, push end_time of start to minHeap
        
        start < minHeap[0]: push end_time of start to minHeap
        
        '''
        
        
        intervals.sort(key=lambda interval:interval[0])
        
        usedRooms=[]
        heapq.heapify(usedRooms)
        
        heapq.heappush(usedRooms, intervals[0][1])
                       
        
        for start,end in intervals[1:]:
            
            if start>= usedRooms[0]:
                heapq.heappop(usedRooms)
            heapq.heappush(usedRooms, end)
                
                
        return len(usedRooms)
     