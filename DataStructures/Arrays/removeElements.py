
'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if val not in nums:
             return len(nums)

        else:

            i=0
            count=0
            idx=len(nums)-1

            while i<len(nums)-1 and i<=idx:
                if nums[i]==val:
                    nums.insert(len(nums),nums[i])
                    nums.pop(i)
                    idx-=1

                else:
                    i+=1
                    count+=1

        return count
        
