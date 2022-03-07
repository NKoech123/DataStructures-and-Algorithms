class Solution:
    def minWindow(self, s: str, t: str) -> str:
     
        #base case
        if t=="": return ""
        
        #creating target map
        target_map,window_map={},{}
        for char in t:
            target_map[char]=1+target_map.get(char,0)
        

        have,need=0,len(t)
        res,resLen=[-1,-1], float("infinity")
        l=0
        for r in range(len(s)):
            window_map[s[r]] = 1 + window_map.get(s[r],0)
         
            
            if s[r] in target_map and target_map[s[r]]==window_map[s[r]]:
                have+=1
              
            
            while have==need :
              
                #update result
                if resLen > r-l+1 :
                    resLen=r-l+1
                    res=[l,r]
                    
                #pop from the left of the window
                window_map[s[l]]-=1
                
                if s[l] in target_map and window_map[s[l]]<target_map[s[l]]:
                    have-=1
                l+=1
                    
        l,r=res  
        return s[l:r+1] if resLen!=float('infinity') else ''
            
