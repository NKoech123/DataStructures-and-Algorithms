class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        logic:
        using sliding window technique
          -create hashmap to track count of characters at every window
          -in any window, in inorder to obtain the longest repeating characters, it makes sense to replace the least characters and 
          leave the most characters. If the least characters in a window is more than K, let's shrink the window from the left my decrementing the 
          leftmost character and incrementing the left pointer by 1. Then store the max size of the window
        
        "A   A   B   A   B   B    A"
        LR
         count={'A':1}
        '''
        
        
        size=0
        count={}
        
        l=0
        
        for r in range(len(s)):
            
            if s[r] in count:
                count[s[r]]+=1
            else:
                count[s[r]]=1
                
            #main logic here - if least replaceable chars are more than K, then you need to shrink that window
            while ((r-l+1) - max(count.values())) > k: 
                
                count[s[r]]-=1
                l+=1
                
            size= max (size , r-l+1)
            
        return size
                
        
