class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda interval:interval[0])
        
        res = [[intervals[0][0],intervals[0][1]]]
               
        for start,end in intervals[1:]:
               
            prevEnd = res[-1][1]
       
            if start > prevEnd: #no overlapping
                res.append([start,end])
                
                
            else: #they overlapp
                
                prevEnd = max(prevEnd, end)
             
                res[-1][1] =  prevEnd
              
               
        return res
               