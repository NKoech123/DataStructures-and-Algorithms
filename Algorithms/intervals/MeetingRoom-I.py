class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        '''
        Time Complexity: O(nlogn)
        Space complexity: O(1). Since no additional space is allocated
        
        0.....................30(prevEnd)
            5..10   15..20
          
       
        '''
        if not intervals:
            return True
        
        intervals.sort(key = lambda interval:interval[0])
        
        prevEnd = intervals[0][1]
        
        for start,end in intervals[1:]:
            
            if start < prevEnd:
                return False
            else:
                prevEnd = end
                
        return True
   