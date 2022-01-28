class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        we could compare s and its reverse s[::-1] to determine if s is palidrome or not, but that will result in creating extra space 0(len(s)).
        For in-place operation, see solution below:
        
        '''
        
        i , j = 0 , len(s)-1
        
        while i<j:
            
            
            while i<j and not s[i].isalnum() :
                i+=1
                
            while i<j and not s[j].isalnum():
                j-=1
                
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
            
        return True
