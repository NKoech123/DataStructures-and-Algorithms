class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res=[]
        
        for i in range(len(intervals)):
            
            #check if newInterval can be inserted before the entire intervals list
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            #check if newInterval comes after interval intervvals[i]
            elif newInterval[0]  > intervals[i][1]:
                res.append(intervals[i])
                
            else:
                newInterval = [min(newInterval[0],intervals[i][0]) , max(newInterval[1],intervals[i][1])]
                
        res.append(newInterval)
        
        return res
