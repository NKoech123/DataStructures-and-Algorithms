class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices = [7, 1, 5, 3, 6, 4]
        
        -buy on first day 
        -instatiate max_profit
        -check if the next day prices are lower than buying:
             -if future prices are lower, replace future buy price with curr buy   
        - return max_profit
        
        Time- O(N)
        Space- O(1)
        '''
        
        buy=prices[0]
        
        max_profit=0
        
        for i in range(1,len(prices)):
            
            if buy>prices[i]:
                buy=prices[i]
            else:
                max_profit=max(max_profit,prices[i]-buy)
                
        return max_profit
  
            
