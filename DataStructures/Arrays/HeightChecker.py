#Leetcode problem 1051
class Solution:
    def heightChecker(self, heights: List[int]) -> int:

    
        sum=0
        for i,j in zip(heights,sorted(heights)):
            if i!=j:
               sum+=1
        return sum
