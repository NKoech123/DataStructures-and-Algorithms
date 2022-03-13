class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        '''
        Time Complexity: O(nlogn)
        Space complexity: O(1). Since no additional space is allocated
        
        
        '''
        if len(intervals)<=1:
            return True
        
        intervals.sort(key=lambda i:i[0])
        prevEnd = intervals[0][1]
        
        for start,end in intervals[1:]:
            
            if start<prevEnd:
                return False
            prevEnd=end
            
        return True
        
