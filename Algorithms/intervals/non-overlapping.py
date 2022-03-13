class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #sorting by starting point
        intervals.sort(key=lambda i:i[0])
        overlap = 0
        prevEnd = intervals[0][1]
        
        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end
            
            else:
                overlap+=1
                prevEnd = min (prevEnd, end)
            
      
        return overlap
