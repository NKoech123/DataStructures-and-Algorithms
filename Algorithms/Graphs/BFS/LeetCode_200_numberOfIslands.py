class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        -traversing the grid O(M*N)
             -when grid[r][c]=="1", ++islands(was instatiate as 0) and go bfs(r,c) / mark all 
             grid cells connected to that "incremented" island
             
        -bfs(r,c)  (iterative) we will create a Queue
               -append grid position (r,c) to the Q
               -create a while loop
                     -pop the leftmost/earliest added grid position
                     -find the neighboring grid cell locations and check if 
                      they fullfil req: (1) within location limits (2) cell contains '1'/ it's land/it's an extension
                                        incremented island
                     -for all neighboring locations that fulfill req, replace the "1" grid cell with '0', then add that
                      location to the Queue. We want to make the Q full.
                               
        
        '''
        
        ROWS,COLS= len(grid),len(grid[0])
        islands=0
        
        Q=deque([])
        def bfs(r,c):
            
            Q.append((r,c))
            
            while Q:
                
                row,col = Q.popleft()
                           #right, left,   up,   down
                directions=[(0,1),(0,-1),(-1,0),(1,0)] 
                
                for dr,dc in directions:
                    new_row,new_col = dr+row , dc+col
                    
                    if (new_row >=0 and new_row < ROWS and new_col >=0 
                        and new_col < COLS and grid[new_row][new_col]=="1"):

                        grid[new_row][new_col]="0"
                        Q.append((new_row,new_col))
            
            
        if not grid or len(grid)==0:
            return 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    islands+=1
                    bfs(r,c)
                    
        return islands
            
        

