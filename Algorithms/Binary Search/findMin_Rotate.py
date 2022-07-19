'''
using array=[1,2] let's use two permutations as an example.
First case is when arr= [1,2] 
      [1,     2]
       l/m    r
       if nums[m] < nums[m+1]: return nums[m]. This comes first since we write nums[m-1] for when m=0 causing nums[-1].
       
 Second case is when arr = [2,1]
        [2,  1]
        l/m.  r
        if nums[m] < nums[m-1]: return nums[m]

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        nums = [3, 4, 5, 1, 2]
        [1,2,3]
        [2,1]
           lr
           m
        
        [1,2]
        l   r
           m
         if nums[m] > nums[m+1]: return nums[m+1]
         if nums[m] > nums[m-1]: return nums[m-1]
        '''
        l,r = 0, len(nums)-1
        
        if (nums[0]<nums[r] or 
            len(nums) == 1): 
            return nums[0]
        
        while l<=r:
            m = l+ (r-l)//2
            
            if nums[m] > nums[m+1]:
                return nums[m+1]
            if nums[m] < nums[m-1]:
                return nums[m]
            
            if nums[m] > nums[0]:
                l=m+1
            else:
                r=m-1
    
    #recursive solution
    def recu_findMin(self, nums):
        if len(nums) == 1: return nums[0]
        
        mid = len(nums) // 2
        left_comp, right_comp = nums[mid - 1], nums[len(nums) - 1]
        
        if left_comp < right_comp: return self.recu_findMin(nums[0:mid])
        
        else: return self.recu_findMin(nums[mid:len(nums)])

            



