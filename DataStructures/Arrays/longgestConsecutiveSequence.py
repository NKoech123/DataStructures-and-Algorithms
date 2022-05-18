class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        set = {100,4,200,1,3,2}
        
        '''
        
        curr_streak, longest_streak = 0, 0
       
        num_set = set(nums)
        
        for num in num_set:
            
            if num-1 not in num_set:
                curr_num = num
                curr_streak= 1
                
                while curr_num + 1 in num_set:
                    curr_num+=1
                    curr_streak+=1
                    
                longest_streak = max(longest_streak, curr_streak)
                
        return longest_streak
