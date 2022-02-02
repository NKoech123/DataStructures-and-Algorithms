class Solution:
    def isValid(self, s: str) -> bool:
        '''
        tests stacks
        
        s="{[]}"
        
        s="()[]{}"
        
        Time O(N) - linear time thru' iterating string s
        Space O(N) - because of stack
        '''
        
        stack=[]
        
        closeToOpen=  {")": "(", "}": "{", "]": "["}
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                    
                else:
                    return False
            else:
                stack.append(c)
                
        return True if not stack else False
            
