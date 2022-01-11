class Solution:
    #iterative solution
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[l] < nums[mid]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                return nums[l]
        return nums[l]
    
    #recursive solution
    def recu_findMin(self, nums):
        if len(nums) == 1: return nums[0]
        
        mid = len(nums) // 2
        left_comp, right_comp = nums[mid - 1], nums[len(nums) - 1]
        
        if left_comp < right_comp: return self.recu_findMin(nums[0:mid])
        
        else: return self.recu_findMin(nums[mid:len(nums)])

            



