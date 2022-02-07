
'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        nums1 In-place instead.
        """
        i=m-1
        idx=len(nums1)-1
        j=n-1

        while j>=0 and i>=0:  #2

            if nums2[j]>=nums1[i]:
                nums1[idx]=nums2[j]
                idx-=1
                j-=1

            elif nums2[j]<=nums1[i]:
                 nums1[idx]=nums1[i]
                 i-=1
                 idx-=1

        if j>=0:
            nums1[:j+1] = nums2[:j+1]


        return nums1
