#leetCode 20
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        -if char is opening,append it to stack
        -if char is closing and stack is not empty,  and it's value on hashmap is equal to value to top_element on stack,
         then pop top-most stack element
        -else just return False
        -ultimately after the loop end, return True if stack is empty. If stack is not empty, just return False
        
        '''
       
        
        hashmap= {  '(':')' ,'{':'}', '[':']' }
           
               
        stack=[]
        
        for i in range(len(s)):
                  
            if s[i] in hashmap:
                  stack.append(s[i])
                    
            elif stack and s[i] == hashmap[stack[-1]]:
               
                    stack.pop()
            else:
                  return False
                  
        return True if not stack else False
     
