class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
         s = "catsandog"
         wordDict = ["cats","dog","sand","and","cat"]  FALSE
         
         s = "applepenapple"
         wordDict = ["apple","pen"]  TRUE
        
         s = "leetcode"
         wordDict = ["leet","code"]     TRUE
        
        dp=[True False False False False False ]
        '''
        
        word_set=set(wordDict)
        
        dp= [False] * (len(s) + 1)
        dp[0]=True
        
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i]=True
                    break
        return dp[len(s)]
    
    
 
    def wordBreak_reverse(self, s: str, wordDict: List[str]) -> bool:
        '''
       "dog","sand","and","cat"]  FALSE
         
         s = "applepenapple"
         wordDict = ["apple","pen"]  TRUE
        
         s = "leetcode"
         wordDict = ["leet","code"]     TRUE
         
             "l    e     e     t     c     o     d      e"
        dp=[False False False False True False False False True ]
                                     i   
        '''
        dp = [False]* (len(s)+1)
        
        dp[len(s)] = True
        
        for i in reversed(range(len(s))):
            for w in wordDict:
                if ( (i+len(w)) <= len(dp) 
                    and s[i:i+len(w)] == w):
                    
                    dp[i] = dp[i+len(w)]
                    
                if dp[i]:
                    break
                    
        return dp[0]
                    
