class Solution:
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
     
        def twoSum(i ,target):

            hashmap , arr = {} ,[]

            j=i+1

            for k in range(j,len(nums)):
                comp = target - nums[k]

                if nums[k] in hashmap:
                    val_1 = nums[i]
                    val_2 = nums[k]
                    val_3 = nums[hashmap[nums[k]]]
                   
                    arr=sorted([val_1, val_2 , val_3])

                    if arr not in res:
                        res.append(arr)
                        
                else:
                    
                    hashmap[comp] = k
                
        res=[]
        
        for i in range(len(nums)):
            
            twoSum(i ,-nums[i])
            
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        (i)Sort nums.If first elem(i) is >0, then the remaining right ones aren't      worth evaluating. If i==0 or if two subsequent elem aren't same, first two sum of them
        remaining (i+1->end)
        (2)Create a two sum func with two-pointers lo=i+1 and hi=len(nums)-1.While lo<hi, traverse the remaining right list while checking if sum[i,lo,hi]==0.If sum>0, hi-=1, If sum<0, lo+=1.Append res and update hi and lo.
        Increase lo+=1, while lo<hi and nums[lo]==nums[lo-1]
        '''
        res=[]
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i]> 0:
                break
            
            if i==0 or nums[i]!=nums[i-1]:
                self.twoSumII(i,res,nums)
        return res
            
        
    def twoSumII(self,i,res,nums):
        lo,hi=i+1,len(nums)-1
        
        while (lo<hi):
            sum=nums[i]+nums[lo]+nums[hi]

            if sum>0:
                hi-=1
            elif sum<0:
                lo+=1
            else:
                res.append([nums[i],nums[lo],nums[hi]])
                hi-=1
                lo+=1
                while lo<hi and nums[lo]==nums[lo-1]:
                    lo+=1
        
    def threeSum_WithSet(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [-1, 0, 1, 2, -1, -4]
                 i  
        '''
        res=set()
        dups=set()
        
        seen={}
        
        for i,val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                
                for j,val2 in enumerate(nums[i+1:]):
                    complement = -val1-val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1,val2,complement))))
                    seen[val2] = i
                    
        return res
                    
