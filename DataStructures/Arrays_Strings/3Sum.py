class Solution:
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
                    
