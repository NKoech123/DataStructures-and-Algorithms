class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        BigHeist=[None for _ in range(len(nums)+1)]
        
        n=len(nums)
        
        #initialize base case
        BigHeist[n]=0
        BigHeist[n-1]=nums[n-1]
        
        #dp table calculation
        for i in range(n-2, -1, -1):
            
            BigHeist[i]= max(BigHeist[i+1],BigHeist[i+2]+nums[i])
            
        return BigHeist[0]
    
    
   class Solution:
    
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        
        return self.robFrom(0, nums)
    
    def robFrom(self,i, nums):
        
        if i>=len(nums):
            return 0
        
        if i in self.memo:
            return self.memo[i]
    
        ans = max(nums[i] + self.robFrom(i+2, nums), 
                  self.robFrom(i+1, nums))
        
        self.memo[i] = ans
        
        return ans  
    
    
    
  class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
 
        [rob1, rob2, n]
               rob1  rob2
        '''
        
        rob1, rob2 = 0, 0
      
        for n in nums:
            
            temp =  max(n + rob1, rob2)
            
            rob1, rob2 = rob2, temp
            
        return rob2
        
      
      
