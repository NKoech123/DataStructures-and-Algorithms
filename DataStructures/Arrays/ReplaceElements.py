#Replace Elements with Greatest Element on Right Side. Source: LeetCode (Easy)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        index=1
        for i in range(0,len(arr)-1):
             arr[i]=max(arr[index:])
             index+=1
        arr[-1]=-1
        return arr
