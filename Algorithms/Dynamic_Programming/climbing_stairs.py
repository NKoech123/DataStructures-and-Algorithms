class Solution:
    def climbStairs(self, n: int) -> int:
       
        cache={1:1,2:2}
        return self.climb(n,cache)
        
    
    def climb(self,n,cache):

        if n in cache:
            return cache[n]


        answer=self.climb(n-1,cache) + self.climb(n-2,cache)
        cache[n]=answer

        return cache[n]
