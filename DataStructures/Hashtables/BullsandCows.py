class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls,cows=0,0
        allocation_map={}
        
        for i in range(len(secret)):
            if secret[i] in allocation_map:
                allocation_map[secret[i]]+=1
            else:
                allocation_map[secret[i]]=1
                
        for i in range(len(secret)):
            
            if guess[i]==secret[i] and allocation_map[guess[i]]>0:
                bulls+=1
                allocation_map[guess[i]]-=1
                
        for i in range(len(secret)):
            if guess[i]!=secret[i] and guess[i] in allocation_map:
                if allocation_map[guess[i]]>0:
                    cows+=1
                    allocation_map[guess[i]]-=1
                    
        return "{}A{}B".format(bulls,cows)
