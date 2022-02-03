class Solution:
    def countSubstrings(self, s: str) -> int:
        
        '''
        account for odd and even length. traverse the s while making "circles" at each point
        
        Time: O(N*N)
        Space: O(1)
        
        '''
        
        count=0
        
        for i in range(len(s)):
            
            #odd length
            l,r=i,i
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
                
            #even length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
                
                
        return count
                
