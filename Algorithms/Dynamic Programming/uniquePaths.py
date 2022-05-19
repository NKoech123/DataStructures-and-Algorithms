class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        m rows
        n columns
        two decisions to make at each step: down or up
        
        '''
        
        dp =[[1]*n for _ in range(m)]
        
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r][c-1]  + dp[r-1][c] 
                
        return dp[m-1][n-1]
        
