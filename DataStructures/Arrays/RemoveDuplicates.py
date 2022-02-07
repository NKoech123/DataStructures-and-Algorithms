class Solution:
    def removeDuplicates(self, nums) -> int:
         index=1
         if len(nums)==2 and nums[0]!=nums[1]: 
            return len(nums)

         else:
            index=1
            for i in range(1,len(nums)):
                if nums[i]!=nums[i-1]:
                    nums[index]=nums[i]
                    index+=1
            return index
