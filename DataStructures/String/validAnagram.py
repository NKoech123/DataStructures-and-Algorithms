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
        

    def isAnagram_sol2(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        count = [0]*26
        
        for char in s:
            count[ord(char)-ord('a')] +=1
            
        for char in t:
            count[ord(char)-ord('a')] -=1
            if count[ord(char)-ord('a')] < 0:
                return False
            
        return sum(count) == 0
