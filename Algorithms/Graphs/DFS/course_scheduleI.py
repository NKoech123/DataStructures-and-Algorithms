from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
    
        courseDict = defaultdict(list)
      
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        checked, path = [False] * numCourses, [False] * numCourses
       
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, checked, path):
                return False
        return True
    
    def isCyclic(self, currCourse, courseDict, checked, path):
       
        if checked[currCourse]: return False
        if path[currCourse]: return True

        path[currCourse], ret = True ,False

        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, checked, path)
            if ret: break
    
        path[currCourse], checked[currCourse] = False ,True
       
        return ret
