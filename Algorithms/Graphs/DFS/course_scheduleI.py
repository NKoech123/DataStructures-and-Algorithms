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
            
    ###########################################################################################

class Color:
    WHITE = 0,
    GREY = 1,
    BLACK = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [Color.WHITE] * numCourses
        G = collections.defaultdict(list)
        for course, r in prerequisites:
            G[course].append(r)
        
        def dfs(node):
            for prereq in G[node]:
                if visited[prereq] == Color.WHITE:
                    visited[prereq] = Color.GREY
                    dfs(prereq)
                elif visited[prereq] == Color.GREY:
                    raise 
            visited[node] = Color.BLACK
        
        try: 
            for n in range(numCourses):
                if visited[n] == Color.WHITE:
                    visited[n] = Color.GREY
                    dfs(n)
            return True 
        except:
            return False
            
        return True
    
