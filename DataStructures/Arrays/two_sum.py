class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums = [2,3,2, 3,3,3,3,3,7]  target = 9
                    i            j
        hashmap = {}
        
        N*N
        
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                
        [2,7,11,15]  t=9
       
        
          '''
        hashmap = {}
        
        for i in range(len(nums)):
            
            comp = target - nums[i]
            
            if nums[i] in hashmap:
                return [i, hashmap[nums[i]]]
            
            hashmap[comp] = i
            
