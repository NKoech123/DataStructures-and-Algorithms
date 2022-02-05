class Solutions:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices = [7, 1, 5, 3, 6, 4]
                  i  j
        
       -create two loops, i=0:end indicating the buying day and j=i+1:end exploring all the possible sellings.
       days
       -make sure
        
        Time- O(N*N) loop runs n(n-1)/2 times. Very inefficient
        Space- O(1) . Only max_profit variable is used
        '''
        max_profit=0
        
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i] < prices[j]:
                    max_profit=max(max_profit, prices[j]-prices[i])
                    
        return max_profit
    
    
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices = [7, 1, 5, 3, 6, 4]
        -instatiate max_profit
        -buy on first day 
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
  
            
