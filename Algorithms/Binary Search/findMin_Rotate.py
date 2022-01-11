class Solution:
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
