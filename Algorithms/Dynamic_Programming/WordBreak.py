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
