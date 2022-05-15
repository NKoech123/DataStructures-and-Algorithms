class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res
    
    '''Below is another solution without implementing ASCII codes'''
    
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        size=0
        
        for l in range(len(s)):
     
            visited=set()
            r=l
            
            while r<len(s) and s[r] not in visited:
                visited.add(s[r])
                r+=1
                
            size = max (size , r-l)
            visited=set()
            
        return size
    
#I consider this a better solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        "p  w  w  k  e   w"
                  l     
                         r
 
        '''
        l,r, res = 0, 0 , 0
        
        visited = set()
        
        for r in range(len(s)):
            
            while s[r] in visited:
                visited.remove(s[l])
                l+=1
                
            visited.add(s[r])
            res = max(res, r-l+1)
        return res
                
