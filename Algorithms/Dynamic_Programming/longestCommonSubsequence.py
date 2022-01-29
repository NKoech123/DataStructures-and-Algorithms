class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        
        
        
        
        '''
        
        dp= [ [0]*(len(text2)+1) for _ in range(len(text1)+1)]
        
        
        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    #add 1+diagonal in that cell dp[i][j]
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    #add values below and to the right
                    dp[i][j] = max (dp[i][j+1], dp[i+1][j])
                    
        return dp[0][0]
                
