'''
Time 0(s+t+v)
Space 0(N) - for the hashmap
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):  return False
        
        hashmap={s[i]:0 for i in range(len(s))}
        
        for j in range(len(s)):
            hashmap[s[j]]+=1 
        
        for k in range(len(t)):
            if t[k] in hashmap:
                hashmap[t[k]]-=1
        
        for v in hashmap.values():
            if v!=0:
                return False
        return True
