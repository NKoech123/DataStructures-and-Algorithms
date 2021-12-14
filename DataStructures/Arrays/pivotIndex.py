class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        check base case
        '''
        if sum(nums[1:len(nums)])==0:
            return 0
        
        i=1
        while i<=len(nums)-1:

            left_sum=sum(nums[0:i])
            right_sum=sum(nums[i+1:len(nums)])

            if right_sum==left_sum:
                return i
            i+=1

        return -1