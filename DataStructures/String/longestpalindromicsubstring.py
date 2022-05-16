class Solution:
            
    def longestPalindrome(self, s):
     
        longestpalindrome =""
        for c in range(len(s)):
            
            #for odd
            pal=self.getPalindromeLen(s,c,c)
            if len(pal)>len(longestpalindrome):
                longestpalindrome=pal
            
            #for even
            pal=self.getPalindromeLen(s,c,c+1)
            if len(pal)>len(longestpalindrome):
                longestpalindrome=pal
            
        return longestpalindrome
    
    def getPalindromeLen(self ,s ,lo ,hi):
        
        pal=""
        
        while lo>=0 and hi<len(s) and s[lo]==s[hi] :
            
            lo-=1
            hi+=1
            
        pal=s[lo+1:hi]
        
        return pal
            
