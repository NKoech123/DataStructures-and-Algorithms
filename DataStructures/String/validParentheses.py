class Solution:
    def isValid(self, s: str) -> bool:
        '''
        s="{[]}"
        
        s="()[]{}"
        
        stack=['(']
        -create empty stack stack.
        -create a hashmap that close->opening
        -loop thru' the s searching if s[char] in map:
              -if it's in map, that's a closing and so there should be an opening in the stack.
              -if the s[char] is not in the map, means it's an opening,so append it to stack.
        
        '''
        
        stack=[]
        
        closeToOpen={')':'(' ,   '}':'{' ,   ']':'['  }
        
        
        
        for c in s:
            
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
        
            else:
                stack.append(c)
                
        
        return True if not stack else False
