'''
Time 0(s+t+v)
Space 0(N) - for the hashmap
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #when lengths vary,then not an anagram
        if len(s)!=len(t): return False
        
        #create hashmap= {char:count}
        hashmap={}
        for char in s:
            hashmap[char] =1 + hashmap.get(char,0)
        
        #we decreament count for all the chars available in t
        for char in t:
            if char in hashmap:
                hashmap[char]-=1
        #if it's anagram, we will expect all the map values to be zero. if there's any non-zero val, then it's
        #not an anagram
        for val in hashmap.values():
            if val!=0:
                return False
        return True
        
