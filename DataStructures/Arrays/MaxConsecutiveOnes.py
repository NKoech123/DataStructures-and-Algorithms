#Leetcode problem 485

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        arr=[]
        total=0
        for i in range(len(nums)):
            if nums[i]==1:
               total+=1
            else:
                arr.append(total)
                total=0
                
        arr.append(total)
        
        return max(arr)
