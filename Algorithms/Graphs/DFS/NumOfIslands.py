'''
Time complexity : O (M*N)

Space complexity : worst case O(M*N) in case that the grid map is filled with lands where DFS goes by M*N deep.

'''

class Solution:
    def dfs(self,row,col,grid):
        
        
        if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col]=="0":
            return 
        
        grid[row][col]="0"
        
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        
        for x,y in directions:
            new_row,new_col=x+row, y+col
            self.dfs(new_row,new_col,grid)
          
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or len(grid)==0:
            return 0

        num_row, num_col, islands= len(grid), len(grid[0]), 0
        
            
        for r in range(num_row):
            for c in range(num_col):
                
                if grid[r][c]=="1":
                    islands+=1
                    self.dfs(r,c,grid)
                    
                    
        return islands
                           
        
        
        
