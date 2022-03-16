'''
Time complexity : O (M*N)

Space complexity : worst case O(M*N) in case that the grid map is filled with lands where DFS goes by M*N deep.

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS,COLS = len(grid), len(grid[0])
        islands=0
        
        def dfs(grid,r,c):
            
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]=="0":
                return
            
            grid[r][c]="0"
            directions=[(-1,0),(1,0),(0,-1),(0,1)]
            for dr,dc in directions:
                dfs(grid,r+dr,c+dc)
          
        if not grid or len(grid)==0:
            return 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    islands+=1
                    dfs(grid,r,c)
        return islands
        
  
        
        
        
