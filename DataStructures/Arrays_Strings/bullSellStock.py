# LeetCode 121
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max_profit,profit=0,0
        
        for i in range(1,len(prices)):
            
            if prices[i]>buy:
                profit=prices[i]-buy
                max_profit=max(profit,max_profit)
                
            elif prices[i] < buy:
                buy=prices[i]
                
        return max_profit
