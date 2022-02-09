class HitCounter:

    def __init__(self):
        self.storage={}
        

    def hit(self, timestamp: int) -> None:
        
        if timestamp in self.storage:
            self.storage[timestamp]+=1
        else:
            self.storage[timestamp]=1
        
        

    def getHits(self, timestamp: int) -> int:
        
        hits=0
        
        for key in list(self.storage):
            #check if timestamp is in range
            if timestamp-key < 300:
                hits+=self.storage[key]
            
            else: #just for scaling
                del self.storage[key]
                
        return hits
        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
