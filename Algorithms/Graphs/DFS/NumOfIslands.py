from collections import deque
import unittest
class Graph:
    def __init__(self, grid = None):
        self.grid = grid
        self.ROWS = len(self.grid)
        self.COLS = len(self.grid[0])
        self.direction = [(-1,0),(1,0),(0,-1),(0,1)]
        self.islands = 0

    def numIslands_DFS_recursive(self) -> int:
        
        ROWS,COLS = self.ROWS, self.COLS
        islands=0
        grid = self.grid
        
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

    def numIslands_DFS_iterative(self) -> int:
        ROWS,COLS = self.ROWS, self.COLS
        grid = self.grid
        islands = 0
        stack=[]
        

        def dfs(r,c):
            stack.append((r,c))

            while stack:
                r,c =stack.pop()

                grid[r][c]="0"
                for dr,dc in self.direction:
                    row,col = dr+r, dc+c
                    #check location limits and if next location is not visited
                    if ((row >= 0 and row < ROWS 
                        and col >= 0 and col < COLS)
                        and grid[row][col]=="1"):
                        stack.append((row,col))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands+=1
                    dfs(r,c)

        return islands


    def numIslands_BFS_iterative(self) -> int:
        '''
        BFS uses Queue, first in,first out approach. In other words, we will process
        all the neighbors before we go to further neighbors of neighbors
        '''
        Q=deque([])
   
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.grid[r][c] == "1":
                    self.islands+=1
                    Q.append((r,c))

                while Q:
                    r,c = Q.popleft()

                    self.grid[r][c] = "0"

                    for dr,dc in self.direction:
                        row,col = dr+r, dc+c

                        if ((row>=0 and row<self.ROWS
                           and col>=0 and col<self.COLS)
                           and self.grid[row][col]=="1"):

                           Q.append((row,col))
                

        return self.islands

class Test(unittest.TestCase):

    def testfunc_DFS_recursive(self):
    
        expected_numofIslands = 3
        self.assertEqual ( self.runner_DFS_recursive(),  expected_numofIslands)

    def testfunc_DFS_iterative(self):
      
        expected_numofIslands = 3
        self.assertEqual ( self.runner_DFS_iterative(),  expected_numofIslands)
    
    def testfunc_BFS_iterative(self):

        expected_numofIslands = 3
        self.assertEqual ( self.runner_BFS_iterative(),  expected_numofIslands)
   
    
    def runner_DFS_recursive(self):
        grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
        g = Graph(grid)
        
        n_islands=g.numIslands_DFS_recursive()
        return n_islands

    def runner_DFS_iterative(self):
        grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
        g = Graph(grid)
       
        n_islands=g.numIslands_DFS_recursive()
        return n_islands

    def runner_BFS_iterative(self):
        grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
        g = Graph(grid)
      
        n_islands=g.numIslands_BFS_iterative()
        return n_islands
    
if __name__ == "__main__":

    unittest.main()
  
 
