class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        amount -coin
         a=  0 1  2  3              11
        dp= [0 1 12 12 12 12 12 12 12]
        
         c in coins=[1,2,5]
        '''
        dp=[amount+1]*(amount+1)
        dp[0]=0
        
        for a in range(1,len(dp)):
            for c in coins:
                
                if (a-c)>=0:
                    dp[a]= min(dp[a], 1+ dp[a-c])
                    
        return dp[amount] if dp[amount]!=len(dp) else -1
