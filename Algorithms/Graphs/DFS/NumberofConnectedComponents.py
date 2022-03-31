from collections import deque
class Solution:
    
    def __init__(self):
        self.visited=set()

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #Create an AdjList
        adjList = {i:[] for i in range(n)}
        
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            
        components=0
    
        def dfs(node,parent):
            
            if node not in self.visited:
                self.visited.add(node)
            else:
                return
            
            for nei in adjList[node]:
                
                if node==parent:
                    continue
                
                dfs(nei,node)
        
        for node in range(n):
            if node not in self.visited:
                components+=1
                dfs(node,-1)
                
        return components


    def countComponents_bfs(self, n: int, edges) -> int:
        '''
        0:[1]
        1:[0,2]
        2:[1]
        
        visited= { 0,1,2 }
        
        '''
        visited=set()
        queue=deque([])
        count=0
        
        adjlist={i:[] for i in range(n)}
        for a,b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)
        
        def bfs(node):
            queue.append(node)
            
            while queue:
                
                node = queue.popleft()
                
                visited.add(node)
                
                for nei in adjlist[node]:
                    if nei not in visited:
                        queue.append(nei)
                    
        for node in range(n):
            if node not in visited:
                count+=1
                bfs(node)
        return count
       
