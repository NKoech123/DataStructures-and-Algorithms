class Solution:
            
    def longestPalindrome(self, s):
        '''
          
         "b  a  b  a   d"
          
        solve for odd and even strings. Every point behaves like a circle
      
        '''
        res=[]
        
        resLen=0
        
        for i in range(len(s)):
            #odd length
            l,r=i,i
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res=s[l:r+1]
                    resLen=len(res)
                l-=1
                r+=1
                
            #even length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res= s[l:r+1]
                    resLen=len(res)
                l-=1
                r+=1
                
        return res
