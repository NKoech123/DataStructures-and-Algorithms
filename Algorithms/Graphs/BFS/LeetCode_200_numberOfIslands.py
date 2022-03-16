#LeetCode_200
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS,COLS = len(grid), len(grid[0])
        islands=0
        Q=deque([])
        
        
        def bfs(grid,r,c):
          
            Q.append((r,c))
            
            while Q:
                row,col=Q.popleft()
                
                
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    new_row , new_col = dr+row , dc+col
                    if (new_row>=0 and new_row<ROWS and new_col>=0 
                       and new_col<COLS and grid[new_row][new_col]=="1" ):
                            
                        grid[new_row][new_col]="0"
                        Q.append((new_row,new_col))
                
        if not grid or len(grid)==0:
            return 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    islands+=1
                    bfs(grid,r,c)
        return islands
    

