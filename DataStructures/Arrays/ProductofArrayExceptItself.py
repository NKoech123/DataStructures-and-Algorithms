class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
       left and right product lists
        
       left=[1]*len(nums)
       right=[1]*len(nums)
        
        '''
        answer=[1]*len(nums)
        left=[1]*len(nums)
        right=[1]*len(nums)
        
        for i in range(1,len(nums)):
            left[i]=nums[i-1]*left[i-1]
            
        for j in range(len(nums)-2,-1,-1):
            right[j]=right[j+1]*nums[j+1]
            
            
        for k in range(len(nums)):
            answer[k]=right[k]*left[k]
            
        
        return answer
