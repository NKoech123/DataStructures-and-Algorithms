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
