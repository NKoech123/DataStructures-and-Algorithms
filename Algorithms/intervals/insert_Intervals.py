class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        #newInterval[0], newInterval[1]
        n= len(intervals)
        res=[]
        
        for i in range(n):
            
            #if newInterval comes before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
<<<<<<< HEAD
            #if newInterval comes after
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
           
            else: #for overlapping
                newInterval = [min(newInterval[0],intervals[i][0]),
=======
            #check if newInterval comes after interval intervals[i]
            elif newInterval[0]  > intervals[i][1]:
                res.append(intervals[i])
                
            else:
                newInterval = [min(newInterval[0],intervals[i][0]) ,
>>>>>>> 59972b4d04c6e0580fa6383360d1a7b848b32547
                               max(newInterval[1],intervals[i][1])]
                
        res.append(newInterval)
        
        return res
                
                