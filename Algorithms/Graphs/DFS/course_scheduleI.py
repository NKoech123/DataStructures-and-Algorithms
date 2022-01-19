class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        '''
        prerequisites = [[1,0],[0,1]]
        
        preMap={i:[]}
        
        '''
        preMap={i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
            
        #visitSet
        visitSet=set()
        
        def dfs(crs):
          
            if crs in visitSet:  return False  #cycle/loop detected
            
            if preMap[crs]==[]:  return True   #no prereq, so it can be completed
            
            visitSet.add(crs)                  #mark crs as visited
            
            #now check the pre
            for pre in preMap[crs]:
                if dfs(pre)==False: 
                    return False 
            visitSet.remove(crs)
            preMap[crs]=[]
            return True
        
        for crs in range(numCourses): 
            if dfs(crs)==False: 
                return False
            
        return True
    
