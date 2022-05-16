'''
use left and right two-pointers and compare chars from both ends while shrinking. Make sure all
chars are alphanumeric, and assume lower case for comaprison.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l,r = 0,len(s)-1
        
        while l<r:
            
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            
            if s[l].upper() != s[r].upper():
                return False
            l+=1
            r-=1
            
        return True
            
