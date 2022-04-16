class Solution:
    def __init__(self):
        self.cache={1:1,2:2}
        
    def climbStairs_Memoization(self, n: int) -> int:
        return self.climb(n,cache)
        
    def climb(self,n,cache):

        if n in self.cache:
            return self.cache[n]
        
        answer=self.climb(n-1,cache) + self.climb(n-2,cache)
        
        self.cache[n]=answer

        return self.cache[n]
    

    def climbStairs_DP(self, n: int) -> int:
        '''
        1 or 2 ways
        n=5
        dp[n=0]=0
        dp[n=1]=1
        dp[n=2]=dp[n-2] + dp[n-1]=1
        
        dp=[0, 1, 2, 3, 5, 8]
        n=  0, 1, 2, 3, 4, 5
        
        '''   
     
        if n<=2:
            return n
        
        dp= [0]*(n+1)
        
        dp[1]=1
        dp[2]=2
        
        for n in range(3,len(dp)):
            dp[n] = dp[n-1] + dp[n-2]
        return dp[-1]
    
      def climbStairs_iteration(self, n: int) -> int:
        '''
       Time 0(N)
       Space 0(1)
        
        '''   
        p1,p2 = 1,2
        
        if n==p1 of n==p2:
            return n
    
        for _ in range(2,n):
            p1, p2 = p2, p1+p2
        return p2
          
