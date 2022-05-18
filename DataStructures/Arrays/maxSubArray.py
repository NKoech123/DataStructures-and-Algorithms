class Solution:
  
    def maxSubArray_DP(self, nums: List[int]) -> int:
        '''
        Time O(N)
        Space O(N)- storing the array
        
        '''
        
        n=[0 for i in range(len(nums))]
        
        n[0]=nums[0]
        for i in range(1,len(nums)):
            n[i]=max(n[i-1]+nums[i],nums[i])
            
        return max(n)
      

    def maxSubArray_SlidingWindow(self, nums: List[int]) -> int:
        '''
       Time 0(N)
       Space 0(1)
        '''
        maxSub=nums[0]
        currSum=0
        
        for num in nums:
            
            if currSum<0:
                currSum=0
            currSum+=num
            
            maxSub=max(maxSub,currSum)
       
        return maxSub
      

    def maxSubArray_another(self, nums: List[int]) -> int:
        '''  
        
        [5, 4, -1, 7, 8]
            i
           curr_sub= max(nums[i], nums[i]+curr_sub)
       curr_sub = nums[0]
       
       iterate 1:len(nums)
 
    
        '''
        
        curr_sub = nums[0]
        max_sub = nums[0]
        for i in range(1,len(nums)):
            curr_sub = max (nums[i], nums[i]+curr_sub)
            max_sub = max(max_sub, curr_sub)
        return max_sub
