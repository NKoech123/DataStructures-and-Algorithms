'''
Since bucket behaves Linkedlist, we will create Nodes
'''

class Node:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.next=nextNode
        
'''
Bucket acts as a Linkedlist here
'''
class Bucket:
    def __init__(self):
        self.head=Node(0)
        
    def insert(self,newValue):
        #if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode=Node(newValue,self.head.next)
            #set the new head
            self.head.next=newNode
            
    def delete(self,value):
        prev=self.head
        curr=self.head.next
        while curr is not None:
            if curr.value==value:
                #remove the current node
                prev.next=curr.next
                return
            prev=curr
            curr=curr.next
            
    def exists(self,value):
        curr=self.head.next
        while curr is not None:
            if curr.value==value:
                return True
            curr=curr.next
        return False
    
        
        

class MyHashSet:

    def __init__(self):
        '''
        Initialize your data structure here
        '''
        self.keyRange=769  #number of keys
        self.bucketArray=[Bucket() for i in range(self.keyRange)] 
        
    #method to find bucket index
    def _hash(self,key):  
        return key % self.keyRange
    
    #method to add key 
    def add(self, key: int) -> None:
        
        #find the bucket index
        bucketIndex=self._hash(key)
        
        #insert key in that buckIndex
        self.bucketArray[bucketIndex].insert(key)
        
    #method to remove key
    def remove(self, key: int) -> None:
        
        bucketIndex=self._hash(key)
        
        self.bucketArray[bucketIndex].delete(key)
        
    #method to identify if a hash set contains a specific key
    def contains(self, key: int) -> bool:
        bucketIndex=self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
        


    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)