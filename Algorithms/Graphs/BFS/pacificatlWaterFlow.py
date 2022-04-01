
from collections import deque

class Solution:
    def pacificAtlantic(self, heights) :
        
        
        
        ROWS, COLS =len(heights),len(heights[0])
        direction= [(0,1),(0,-1),(1,0),(-1,0)]
  
        pacific_queue = deque()
        atl_queue = deque()
        for r in range(ROWS): #pac, atl
            pacific_queue.append((r,0))
            atl_queue.append((r,COLS-1))
            
        for c in range(COLS):
            pacific_queue.append((0,c))
            atl_queue.append((ROWS-1,c))
        
            
        Q=deque([]) 
        
        def bfs(Q):
            
            
            reachable =set()
            
            while Q:
                
                r,c = Q.popleft()
                
                reachable.add((r,c))
                
                #let's check for neighbors within
                #direction limit and greater than prev
                for dr,dc in direction:
                    
                    row,col = r+dr,c+dc
                    #check for limit bounds, water direction(height), 
                    #we visit the unvisited spots
                    if ((row>=0 and row<ROWS and col>=0 and col<COLS)
                        and (heights[r][c] <= heights[row][col]) 
                        and ((row,col) not in reachable)):
                        
                        Q.append((row,col))
                        
            return reachable
        
        pacific_reachable, atl_reachable  = bfs(pacific_queue), bfs(atl_queue)
        
        return list(atl_reachable.intersection(pacific_reachable))
        