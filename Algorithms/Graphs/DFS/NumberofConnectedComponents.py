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
       
