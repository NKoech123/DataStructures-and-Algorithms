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
      
      
