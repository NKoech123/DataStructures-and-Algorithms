class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        
        
        1....2(prevEnd)
             2(start)....3(end)
                    
        1...3(prevEnd)
          2(start)....4(end)
          
         1..........6
            2...4
        
        
        -sort the intervals by start time
        -indicate the prevEnd = intervals[0][1]
        
        -iterate from i=1:n-1
           if start >= prevEnd: no overlapping
              prevEnd = end
           if start < prevEnd: overlapping
              count+=1
              prevEnd = min(prevEnd, end)
        
        '''
        count = 0
        intervals.sort(key= lambda interval:interval[0])
        
        prevEnd = intervals[0][1]
        
        for start,end in intervals[1:]:
            
            #there's no overlapping
            if start >=prevEnd:
                prevEnd = end
                
            else:
                count+=1
                prevEnd = min(prevEnd, end)
                
        return count