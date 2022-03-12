class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
        
        for start,end in intervals[1:] :
            
            lastEnd = output[-1][1]
            
            if lastEnd >= start: #they overlapp  [1,5] +  [2,4] = [1,5]
                output[-1][1]= max(lastEnd,end)
                
            else:
                output.append([start,end]) #no overlapping
                
        return output
