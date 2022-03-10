#LeetCode 345
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import defaultdict
        
        mp={} #num->count
        bucket=defaultdict(list)
        bucket={i+1:[] for i in range(len(nums))}
        
        for num in nums:
            mp[num] = 1 + mp.get(num,0)
         
        #bucket count->num    
        for num,counts in mp.items():
            bucket[counts].append(num)
            
        #let's get the k most frequent elements
        arr=[]
        for count in range(len(bucket),0,-1):
          
            arr+=bucket[count]

            if len(arr)==k:
                return arr
