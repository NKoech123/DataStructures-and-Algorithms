#LeetCode 33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            m = l + ( r - l ) // 2
            
            if nums[m] == target:
                return m
            
            elif nums[m] >= nums[l]: #we can trust this scope for info
                if nums[l]<=target and nums[m] > target:
                    r=m-1
                else:
                    l=m+1
                
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
             
        return -1