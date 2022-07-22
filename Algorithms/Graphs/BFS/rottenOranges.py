class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        rotten = collections.deque([])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        minutes = 0
        if fresh == 0:
            return minutes
        
        while rotten and fresh:
            l = len(rotten)
            while l:
                l -= 1
                i, j = rotten.popleft()
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    rotten.append((i - 1, j))
                    fresh -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    rotten.append((i + 1, j))
                    fresh -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    rotten.append((i, j - 1))
                    fresh -= 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    rotten.append((i, j + 1))
                    fresh -= 1
            minutes += 1
        return -1 if fresh else minutes    
            
