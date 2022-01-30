class Solution:
    def findMin(self, nums: List[int]) -> int:
        ''' 
        Time 0(log N)
         
         if nums[0]<m:  l=m+1
         if nums[0]>m:  r=m-1
         
         if m<r: m-=1, r=m
         
         if nums[m-1]>nums[m]: return nums[m]
         
         if nums[m]>nums[m+1]: return nums[m+1]
        
        
       
        '''
        if len(nums)==1:
            return nums[0]
        
        l,r = 0, len(nums)-1
        
        if nums[l]<nums[r]:
            return nums[l]
        
        while l<=r:
            m=l+(r-l)//2
            
            if nums[m]<nums[m-1]:
                return nums[m]
        
            if nums[m]>nums[m+1]:
                return nums[m+1]
            
            if nums[0]<nums[m]:
                l=m+1
            else:
                r=m-1
            
