#Incomplete- Not all testacases work
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #base case
        if len(edges) != n-1: return False
        #create adjList
        adj={c:set() for arr in edges for c in arr}
        
        for i in range(len(edges)):
            #build adjacent list
            adj[ edges[i][0]  ].add( edges[i][1] )
            
        #create a dfs
        
        visit=set()
        
        def dfs(c):
            
            if c in visit: return 
            visit.add(c)
            
            for nei in adj[c]:
                dfs(nei)
                
        for c in adj:
            dfs(c)
        return len(visit)==n
        
            
