class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        -create hashset. traverse the list as you add each element to hashset if not present. if elem is present in hashset, then return true.
        -Time O(N) -linear time traversing the array
        -Space O(N)- space used with the elements of the hashtable
        
        
        '''
        
        visit=set()
        
        for num in nums:
            if num in visit:
                return True
            visit.add(num)
            
        return False
