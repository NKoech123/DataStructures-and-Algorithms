class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        l,r=0,len(nums)-1
        mid=l+(r-l)//2
        
        IF nums[l] < nums[m] 
            check if target found in this sorted range. if true r=m-1
            else: l=m+1
            
        ELSE:
           check if target is found between nums[m] and nums[r] : l=m+1
           else: r=m-1
           
          time  O(log n)
          space 0(1)
      
        '''
        
        l,r=0,len(nums)-1
        
        while l<=r:
            
            mid = l+ (r-l)//2
            
            if nums[mid]==target:
                return mid
            
            if nums[l] <= nums[mid] : #left-side of mid is sorted / non-rotated side

                if nums[l]<=target and target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
                    
            else:  #right-side  of mid is sorted
                if target>=nums[mid]  and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
                    
        return -1
                
