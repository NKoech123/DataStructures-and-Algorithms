class Solution:
    def __init__ (self):
        self.cache={0:0,1:1}
    
    
    def fib(self, n: int) -> int:
        
        return self.fibb(n,self.cache)
    
    def fibb(self,n, cache):
        
        if n in self.cache:
            return self.cache[n]
        
        answer=self.fibb(n-1,self.cache)+self.fibb(n-2,self.cache)
        
        self.cache[n]=answer
        
        return self.cache[n]
