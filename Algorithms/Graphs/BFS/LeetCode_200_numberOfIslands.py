#LeetCode_200
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Time: O(R*M)
        Space: O(min(M,N))
        
        '''
        rows = len(grid) # take number of rows
        cols = len(grid[0]) # otherwise take the columns
        if not rows: # if there is no row means empty grid
            return 0
       
        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1 # increase the count
                    grid[r][c] = "0" # sink the island, means marking it down
                    self.bfs(grid,rows,cols,r,c)
        return num_islands
                     

    def bfs(self, grid, rows, cols, r, c):

        Q = deque([])
        Q.append((r,c))
        
        # now until this Q is empty 
        while Q:
           
            row, col = Q.popleft()
            
             ''' check neigbors,if neigbors exist: visit(turn to "0",then append neighbor to Queue)'''
            if row-1 >= 0 and grid[row-1][col] == "1":
                grid[row-1][col] = "0"
                Q.append((row-1,col))
                
            if row+1 < rows and grid[row+1][col] == "1":
                grid[row+1][col] = "0"
                Q.append((row+1,col))
                
            if col-1 >= 0 and grid[row][col-1] == "1":
                grid[row][col-1] = "0"
                Q.append((row,col-1))
                
            if col+1 < cols and grid[row][col+1] == "1":
                grid[row][col+1] = "0"
                Q.append((row,col+1))
    

