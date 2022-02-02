class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        use left and right two-pointers and compare chars from both ends while shrinking. Make sure all
        chars are alphanumeric, and assume lower case for comaprison.
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
