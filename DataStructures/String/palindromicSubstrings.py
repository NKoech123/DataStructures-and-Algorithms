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
  
    def countSubstrings_another(self, s: str) -> int:
        
        count = 0
        
        for i in range(len(s)):
            
            #odd
            count += self.countPalindrome(s, i, i)
            
            #even
            count += self.countPalindrome(s, i, i+1)
            
        return count
    
    
    def countPalindrome(self, s, lo, hi):
        
        count = 0
        
        while lo>=0 and hi<len(s) and s[lo] == s[hi]:
            count +=1
            lo-=1
            hi+=1
            
        return count
