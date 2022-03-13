class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals)==0:
            return 0
        
        intervals.sort(key=lambda x:x[0])
        
        free_rooms=[]
        
        heapq.heappush(free_rooms, intervals[0][1])
        
        
        for interval in intervals[1:]:
            
            start_time=interval[0]
            end_time=interval[1]
            
            if start_time >=free_rooms[0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, end_time)
            
        return len(free_rooms)
                
        
