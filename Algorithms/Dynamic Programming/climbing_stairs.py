class Solution:
    def __init__(self):
        self.cache={1:1,2:2}
        
    def climbStairs(self, n: int) -> int:
        return self.climb(n,cache)
        
    def climb(self,n,cache):

        if n in self.cache:
            return self.cache[n]
        
        answer=self.climb(n-1,cache) + self.climb(n-2,cache)
        
        self.cache[n]=answer

        return self.cache[n]
