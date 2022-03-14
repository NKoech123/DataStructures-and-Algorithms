class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastPos = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            
            if i + nums[i] >= lastPos:
                lastPos= i
                
        return True if lastPos==0 else False
            
