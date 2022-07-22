class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ''' 
        s = "A D O B E C  O D  E B A  N  C"
             lr
        
        '''
        
        if t =='' or s == '' : return ''
        
        target_map = {}
        
        for char in t:
            target_map[char] = 1 + target_map.get(char,0)
                
        need, have = len(target_map) , 0
        
        window_map = {}
        res, resLen = [-1,-1], float("infinity")
        l=0
        for r in range(len(s)):
            window_map[s[r]] = 1 + window_map.get(s[r],0)
  
            if s[r] in target_map and window_map[s[r]] == target_map[s[r]]:
                have+=1
                
            while have == need:
                
                if r-l+1 < resLen:
                    res =[l,r]
                    resLen = r-l+1
                
                window_map[s[l]]-=1
            
                if s[l] in target_map and window_map[s[l]] < target_map[s[l]]:
                    have-=1
                l+=1
                    
        l,r = res
        
        return s[l:r+1] if resLen!= float('infinity') else ''
            
