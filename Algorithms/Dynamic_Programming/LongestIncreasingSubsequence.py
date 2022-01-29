class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        -Start from the end because that's the min LIS we will ever have. 
        
        
        For instance:
        nums=[1,2,4,3]
        
        nums[i=3] has no other value on the right but itself
        LIS[3]=0
        
        nums[i=2] has no other value on the right but itself
        LIS[2]=1        no number in the right of nums[2]  
        
        LIS[2]= max(LIST[2], 1+LIST[2+1]) but !(nums[2]< nums[3])
        
        -0 (N^2)
        
        '''
        
        LIS=[1] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                
                if nums[i]<nums[j]:
                    LIS[i]= max(LIS[i], 1+LIS[j])
                    
        return max(LIS)
        
